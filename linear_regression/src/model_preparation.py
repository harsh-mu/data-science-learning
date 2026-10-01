"""Combine the cleaned, non-summary sources into monthly modeling datasets.

Run after ``data_cleaning.py``:
    python3 linear_regression/src/model_preparation.py
"""

from __future__ import annotations

import re
from pathlib import Path

import pandas as pd


class NaturalGasModelDataBuilder:
    """Build master and complete-case monthly datasets for regression work.

    ``natural_gas_monthly_all_sources.csv`` is an outer join: it preserves all
    observations and therefore shows genuine source-coverage gaps.
    ``natural_gas_monthly_model_ready.csv`` is an inner join: it is the
    complete-case starting point for a first regression model.
    """

    SOURCE_FILES = {
        "henry_hub": "henry_hub_gas_spot_price_cleaned.csv",
        "consumption": "nat_gas_consume_cleaned.xlsx",
        "deliveries": "nat_gas_deliveries_cleaned.csv",
        "production": "nat_gas_production_cleaned.csv",
        "storage": "nat_gas_storage_cleaned.xlsx",
        "weather": "heating_cooling_days_cleaned.xlsx",
    }

    CORE_COLUMN_NAMES = {
        "Henry Hub Natural Gas Spot Price Dollars per Million Btu": "henry_hub_price_usd_per_mmbtu",
        "U.S. Natural Gas Total Consumption (MMcf)": "natural_gas_total_consumption_mmcf",
        "U.S. Natural Gas Deliveries to Electric Power Consumers  Million Cubic Feet": "natural_gas_deliveries_electric_power_mmcf",
        "U.S. Dry Natural Gas Production  Million Cubic Feet": "dry_natural_gas_production_mmcf",
    }

    def __init__(self, cleaned_data_dir: str | Path, model_data_dir: str | Path):
        self.cleaned_data_dir = Path(cleaned_data_dir)
        self.model_data_dir = Path(model_data_dir)

    @staticmethod
    def _snake_case(value: object) -> str:
        value = re.sub(r"[^a-z0-9]+", "_", str(value).casefold())
        return re.sub(r"_+", "_", value).strip("_")

    def _read_source(self, source_name: str, filename: str) -> pd.DataFrame:
        file_path = self.cleaned_data_dir / filename
        if not file_path.exists():
            raise FileNotFoundError(f"Cleaned source not found: {file_path}")
        frame = pd.read_csv(file_path) if file_path.suffix == ".csv" else pd.read_excel(file_path)
        if "Month_Year" not in frame:
            raise ValueError(f"{filename} has no Month_Year column.")
        if frame["Month_Year"].duplicated().any():
            raise ValueError(f"{filename} has duplicate Month_Year values.")

        rename_map = {}
        for column in frame.columns:
            if column == "Month_Year":
                continue
            rename_map[column] = self.CORE_COLUMN_NAMES.get(
                column, f"{source_name}_{self._snake_case(column)}"
            )
        return frame.rename(columns=rename_map)

    def build(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        """Return the all-observations master table and complete-case table."""
        sources = [
            self._read_source(source_name, filename)
            for source_name, filename in self.SOURCE_FILES.items()
        ]
        master = sources[0]
        for source in sources[1:]:
            master = master.merge(source, on="Month_Year", how="outer", validate="one_to_one")

        master["Month_Year"] = pd.to_datetime(master["Month_Year"], format="%d-%m-%Y")
        master = master.sort_values("Month_Year").reset_index(drop=True)
        master["Month_Year"] = master["Month_Year"].dt.strftime("%d-%m-%Y")
        model_ready = master.dropna().reset_index(drop=True)
        return master, model_ready

    def write_datasets(self) -> tuple[Path, Path]:
        self.model_data_dir.mkdir(parents=True, exist_ok=True)
        master, model_ready = self.build()
        master_path = self.model_data_dir / "natural_gas_monthly_all_sources.csv"
        model_ready_path = self.model_data_dir / "natural_gas_monthly_model_ready.csv"
        master.to_csv(master_path, index=False)
        model_ready.to_csv(model_ready_path, index=False)
        return master_path, model_ready_path


if __name__ == "__main__":
    project_dir = Path(__file__).resolve().parents[1]
    builder = NaturalGasModelDataBuilder(
        cleaned_data_dir=project_dir / "cleaned_data",
        model_data_dir=project_dir / "model_data",
    )
    master_path, model_ready_path = builder.write_datasets()
    print(f"Wrote {master_path}")
    print(f"Wrote {model_ready_path}")
