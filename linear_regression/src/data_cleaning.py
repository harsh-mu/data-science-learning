from __future__ import annotations
import csv
from pathlib import Path
import pandas as pd

class NaturalGasDataCleaner:
    """Create cleaned CSV/XLSX files whose tables share a ``Month_Year`` key."""

    SUPPORTED_SUFFIXES = {".csv", ".xlsx", ".xls"}

    def __init__(self, raw_data_dir: str | Path, cleaned_data_dir: str | Path):
        self.raw_data_dir = Path(raw_data_dir)
        self.cleaned_data_dir = Path(cleaned_data_dir)

    @staticmethod
    def _is_date_header(value: object) -> bool:
        return str(value).strip().casefold() in {"date", "day", "month"}

    def _csv_header_row(self, file_path: Path) -> int:
        with file_path.open(newline="", encoding="utf-8-sig") as source_file:
            for row_number, row in enumerate(csv.reader(source_file)):
                if any(self._is_date_header(cell) for cell in row):
                    return row_number
        raise ValueError(f"No Date, Day, or Month header found in {file_path.name}.")

    def _excel_data_sheets(self, file_path: Path) -> dict[str, int]:
        """Find spreadsheet sheets containing a Date/Day/Month header."""
        data_sheets: dict[str, int] = {}
        for sheet_name in pd.ExcelFile(file_path).sheet_names:
            preview = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
            for row_number, row in preview.iterrows():
                if any(self._is_date_header(cell) for cell in row.dropna()):
                    data_sheets[sheet_name] = row_number
                    break
        return data_sheets

    @staticmethod
    def _date_column(frame: pd.DataFrame) -> str:
        for column in frame.columns:
            if str(column).strip().casefold() in {"date", "day", "month"}:
                return column
        raise ValueError("Loaded data does not have a Date, Day, or Month column.")

    @staticmethod
    def _to_numeric_when_possible(series: pd.Series) -> pd.Series:
        """Convert EIA numeric columns while preserving real text columns."""
        if series.dtype.kind in "biufc":
            return series
        normalized = series.replace({"--": pd.NA, "(s)": pd.NA, "": pd.NA})
        numeric = pd.to_numeric(normalized, errors="coerce")
        non_empty = normalized.notna().sum()
        return numeric if non_empty and numeric.notna().sum() / non_empty >= 0.8 else series

    def clean_frame(self, frame: pd.DataFrame, source_name: str) -> pd.DataFrame:
        """Standardize dates, values, and frequency for one source table."""
        frame = frame.dropna(axis=1, how="all").copy()
        dates = pd.to_datetime(frame.pop(self._date_column(frame)), errors="coerce")
        frame = frame.loc[dates.notna()].dropna(how="all").copy()
        dates = dates.loc[frame.index]
        for column in frame.columns:
            frame[column] = self._to_numeric_when_possible(frame[column])

        frame.insert(0, "Month_Year", dates.dt.to_period("M").dt.to_timestamp())
        if frame["Month_Year"].duplicated().any():
            aggregation = "mean" if "henry_hub" in source_name.casefold() else "last"
            frame = frame.groupby("Month_Year", as_index=False).agg(aggregation)

        frame["Month_Year"] = frame["Month_Year"].dt.strftime("%d-%m-%Y")
        return frame.sort_values(
            "Month_Year", key=lambda key: pd.to_datetime(key, format="%d-%m-%Y")
        ).reset_index(drop=True)

    def clean_csv(self, file_path: Path) -> Path:
        frame = pd.read_csv(file_path, skiprows=self._csv_header_row(file_path))
        output_path = self.cleaned_data_dir / f"{file_path.stem}_cleaned.csv"
        self.clean_frame(frame, file_path.stem).to_csv(output_path, index=False)
        return output_path

    def clean_excel(self, file_path: Path) -> Path:
        output_path = self.cleaned_data_dir / f"{file_path.stem}_cleaned.xlsx"
        data_sheets = self._excel_data_sheets(file_path)
        if not data_sheets:
            raise ValueError(f"No data sheet found in {file_path.name}.")
        with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
            for sheet_name, header_row in data_sheets.items():
                frame = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=header_row)
                self.clean_frame(frame, file_path.stem).to_excel(
                    writer, sheet_name=sheet_name[:31], index=False
                )
        return output_path

    def clean_all(self) -> list[Path]:
        if not self.raw_data_dir.is_dir():
            raise FileNotFoundError(f"Raw-data directory not found: {self.raw_data_dir}")
        self.cleaned_data_dir.mkdir(parents=True, exist_ok=True)
        outputs = []
        for file_path in sorted(self.raw_data_dir.iterdir()):
            if file_path.suffix.casefold() == ".csv":
                outputs.append(self.clean_csv(file_path))
            elif file_path.suffix.casefold() in {".xlsx", ".xls"}:
                outputs.append(self.clean_excel(file_path))
        return outputs


if __name__ == "__main__":
    project_dir = Path(__file__).resolve().parents[1]
    cleaner = NaturalGasDataCleaner(
        raw_data_dir=project_dir / "raw_data",
        cleaned_data_dir=project_dir / "cleaned_data",
    )
    for output in cleaner.clean_all():
        print(f"Wrote {output}")
