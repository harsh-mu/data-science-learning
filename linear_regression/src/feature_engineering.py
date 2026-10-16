import pandas as pd
import numpy as np

# Load data
natgas_data = pd.read_csv("model_data/natural_gas_monthly_model_ready.csv")
natgas_data["Month_Year"] = pd.to_datetime(natgas_data["Month_Year"])
natgas_data = natgas_data.sort_values("Month_Year").reset_index(drop=True)

'''
We are going to be creating features to test whether certain lags or seasonality trends can improve model performance.

As a draft, I am thinking to include features such as:
    – Storage Changes
    - Production-Consumption Gap to measure supply-demand balance
    - Storage Lag of 1 month to test if earlier inventories help explain current prices
    - Price Lag of 1 month to test price resistance
    - HDD (Heating Degree Days) Lag 1 month to test delayed weather relationships
    - Month to identify time of year
    - Seasonal sine/cosine to transform month into cyclical values
'''
natgas_data["storage_lag_1"] = natgas_data["storage_weekly_lower_48_states_natural_gas_working_underground_storage_billion_cubic_feet"].shift(1)
natgas_data["storage_change"] = natgas_data["storage_weekly_lower_48_states_natural_gas_working_underground_storage_billion_cubic_feet"] - natgas_data["storage_lag_1"]

print(
    natgas_data[
        ["Month_Year", "storage_lag_1", "storage_change"]
    ].head(10)
)