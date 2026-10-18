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
natgas_data["supply_demand_gap"] = natgas_data["dry_natural_gas_production_mmcf"] - natgas_data["natural_gas_total_consumption_mmcf"]
natgas_data["price_lag_1"] = natgas_data["henry_hub_price_usd_per_mmbtu"].shift(1)
natgas_data["hdd_lag_1"] = natgas_data["weather_heating_degree_days_united_states"].shift(1)
natgas_data["month"] = natgas_data["Month_Year"].dt.month
natgas_data["month_sin"] = np.sin((2 * np.pi * natgas_data["month"]) / 12)
natgas_data["month_cos"] = np.cos((2 * np.pi * natgas_data["month"]) / 12)

# print(natgas_data.columns)

# Data Validation

natgas_data = natgas_data.dropna()

features = [
    "storage_lag_1",
    "storage_change",
    "supply_demand_gap",
    "price_lag_1",
    "hdd_lag_1",
    "month_sin",
    "month_cos"
]

target = "henry_hub_price_usd_per_mmbtu"

model_df = natgas_data[["Month_Year"] + features + [target]].dropna().copy()

# print(model_df.isna().sum())
# print(model_df.shape)
# print(model_df.head())


# Correlation Analysis
corr_matrix = model_df.drop(columns=["Month_Year"]).corr()
price_corr = corr_matrix["henry_hub_price_usd_per_mmbtu"].sort_values(ascending=False)
# print(price_corr)

feature_corr = model_df[features].corr()
# print(feature_corr.round(2))

#                    storage_lag_1  storage_change  supply_demand_gap  price_lag_1  hdd_lag_1  month_sin  month_cos
# storage_lag_1               1.00           -0.27              -0.24        -0.20      -0.25      -0.57       0.65
# storage_change             -0.27            1.00               0.86        -0.04      -0.77      -0.46      -0.69
# supply_demand_gap          -0.24            0.86               1.00        -0.06      -0.66      -0.37      -0.59
# price_lag_1                -0.20           -0.04              -0.06         1.00       0.09      -0.01       0.07
# hdd_lag_1                  -0.25           -0.77              -0.66         0.09       1.00       0.87       0.42
# month_sin                  -0.57           -0.46              -0.37        -0.01       0.87       1.00      -0.00
# month_cos                   0.65           -0.69              -0.59         0.07       0.42      -0.00       1.00



# Running VIF 
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm

X = model_df[features]

X_const = sm.add_constant(X)

vif_df = pd.DataFrame({
    "Feature": X.columns,
    "VIF": [
        variance_inflation_factor(X_const.values, i)
        for i in range(1, X_const.shape[1])
    ]
})

# print(vif_df.sort_values("VIF", ascending=False))

#             Feature        VIF
# 4          hdd_lag_1  31.120571
# 5          month_sin  15.881243
# 6          month_cos   8.204002
# 1     storage_change   8.167779
# 0      storage_lag_1   7.342811
# 2  supply_demand_gap   4.038993
# 3        price_lag_1   1.365798

# Creating chronological train-validation-test split
train_end = int(len(model_df) * 0.6)
val_end = int(len(model_df) * 0.8)
train_df = model_df.iloc[:train_end].copy()
val_df = model_df.iloc[train_end:val_end].copy()
test_df = model_df.iloc[val_end:].copy()

# for name, df in [
#     ("Train", train_df),
#     ("Validation", val_df),
#     ("Test", test_df)
# ]:
#     print(
#         name,
#         df.shape,
#         df["Month_Year"].min(),
#         df["Month_Year"].max()
#     )


'''
Model A: Price Persistance
'''
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, root_mean_squared_error, mean_absolute_error, r2_score

X_train = train_df[["price_lag_1"]]
y_train = train_df[[target]]
X_val = val_df[["price_lag_1"]]
y_val = val_df[[target]]
X_test = test_df[["price_lag_1"]]
y_test = test_df[[target]]

model_a = linear_model.LinearRegression()

model_a.fit(X_train, y_train)
intercept = model_a.intercept_
coefficient = model_a.coef_

y_val_pred = model_a.predict(X_val)
mse = mean_squared_error(y_val, y_val_pred)
rmse = root_mean_squared_error(y_val, y_val_pred)
mae = mean_absolute_error(y_val, y_val_pred)
r_squared = r2_score(y_val, y_val_pred)

# print("Intercept:", intercept)
# print("Coefficient:", coefficient)
# print("Validation MSE:", mse)
# print("Validation RMSE:", rmse)
# print("Validation MAE:", mae)
# print("Validation R²:", r_squared)

# Intercept: [0.43948339]
# Coefficient: [[0.85979166]]
# Validation MSE: 0.9677564508039637
# Validation RMSE: 0.983746131277762
# Validation MAE: 0.6747853359301249
# Validation R²: 0.7684386620028488


# Naive baseline: next month's price = previous month's price
y_naive_pred = val_df["price_lag_1"]

naive_mse = mean_squared_error(y_val, y_naive_pred)
naive_rmse = root_mean_squared_error(y_val, y_naive_pred)
naive_mae = mean_absolute_error(y_val, y_naive_pred)
naive_r2 = r2_score(y_val, y_naive_pred)

# print("Naive MSE:", naive_mse)
# print("Naive RMSE:", naive_rmse)
# print("Naive MAE:", naive_mae)
# print("Naive R²:", naive_r2)

'''
Model B: All Engineered Features
'''

# Define predictors
features_b = [
    "storage_lag_1",
    "storage_change",
    "supply_demand_gap",
    "price_lag_1",
    "hdd_lag_1",
    "month_sin",
    "month_cos"
]

# Prepare training and validation data
X_train_b = train_df[features_b]
X_val_b = val_df[features_b]

y_train_b = train_df[target]
y_val_b = val_df[target]

# Train model
model_b = linear_model.LinearRegression()
model_b.fit(X_train_b, y_train_b)

# Generate validation predictions
y_val_pred_b = model_b.predict(X_val_b)

# Evaluate performance
mse_b = mean_squared_error(y_val_b, y_val_pred_b)
rmse_b = root_mean_squared_error(y_val_b, y_val_pred_b)
mae_b = mean_absolute_error(y_val_b, y_val_pred_b)
r2_b = r2_score(y_val_b, y_val_pred_b)

# Display results
# print("\n--- Model B: All Engineered Features ---")
# print("Intercept:", model_b.intercept_)
# print("MSE:", mse_b)
# print("RMSE:", rmse_b)
# print("MAE:", mae_b)
# print("R²:", r2_b)

# Display coefficients
coefficients_b = pd.Series(
    model_b.coef_,
    index=features_b
)

# print("\nModel B Coefficients:")
# print(coefficients_b.sort_values())

# --- Model B: All Engineered Features ---
# Intercept: 1.6393773637061417
# MSE: 0.903588054976962
# RMSE: 0.9505724880181217
# MAE: 0.6615837723182487
# R²: 0.783792648620543

# Model B Coefficients:
# hdd_lag_1           -1.503985e-03
# storage_change      -4.916076e-04
# storage_lag_1       -2.211153e-04
# supply_demand_gap   -3.541289e-07
# month_cos            1.048115e-01
# month_sin            1.769811e-01
# price_lag_1          8.333034e-01

'''
Model C: Reduced Engineered Features
'''

features_c = [
    "storage_lag_1",
    "supply_demand_gap",
    "price_lag_1",
    "month_sin",
    "month_cos"
]

# Prepare data
X_train_c = train_df[features_c]
X_val_c = val_df[features_c]

y_train_c = train_df[target]
y_val_c = val_df[target]

# Train model
model_c = linear_model.LinearRegression()
model_c.fit(X_train_c, y_train_c)

# Predict
y_val_pred_c = model_c.predict(X_val_c)

# Evaluate
mse_c = mean_squared_error(y_val_c, y_val_pred_c)
rmse_c = root_mean_squared_error(y_val_c, y_val_pred_c)
mae_c = mean_absolute_error(y_val_c, y_val_pred_c)
r2_c = r2_score(y_val_c, y_val_pred_c)

# print("\n--- Model C: Reduced Features ---")
# print("MSE:", mse_c)
# print("RMSE:", rmse_c)
# print("MAE:", mae_c)
# print("R²:", r2_c)

# Coefficients
coefficients_c = pd.Series(
    model_c.coef_,
    index=features_c
)

# print("\nModel C Coefficients:")
# print(coefficients_c)

# --- Model C: Reduced Features ---
# MSE: 1.0265448612100494
# RMSE: 1.0131855018751745
# MAE: 0.7222728801797926
# R²: 0.7543719792532275

# Model C Coefficients:
# storage_lag_1       -1.044295e-04
# supply_demand_gap   -4.460270e-07
# price_lag_1          7.982082e-01
# month_sin           -2.171293e-01
# month_cos           -1.043280e-01

'''
With these 3 models, we have found that using all the engineered features gives the best performance so far, 
beating out a simple prediction using price lag and taking out HDD and Storage Change. Now we will finish the
training of model b using both training and validation observations
'''


'''
Final Evaluation: Model B
'''

# Combine training and validation data
train_val_df = pd.concat(
    [train_df, val_df],
    axis=0
)

# Prepare predictors and target
X_train_final = train_val_df[features_b]
y_train_final = train_val_df[target]

X_test_final = test_df[features_b]
y_test_final = test_df[target]

# Retrain selected model
final_model = linear_model.LinearRegression()
final_model.fit(X_train_final, y_train_final)

# Predict on untouched test set
y_test_pred = final_model.predict(X_test_final)

# Evaluate
test_mse = mean_squared_error(y_test_final, y_test_pred)
test_rmse = root_mean_squared_error(y_test_final, y_test_pred)
test_mae = mean_absolute_error(y_test_final, y_test_pred)
test_r2 = r2_score(y_test_final, y_test_pred)

# print("\n--- Final Model B: Test Results ---")
# print("MSE:", test_mse)
# print("RMSE:", test_rmse)
# print("MAE:", test_mae)
# print("R²:", test_r2)

# Naive forecast on the same test period
y_test_naive = test_df["price_lag_1"]

# print("\n--- Naive Forecast: Test Results ---")
# print("MSE:", mean_squared_error(y_test_final, y_test_naive))
# print("RMSE:", root_mean_squared_error(y_test_final, y_test_naive))
# print("MAE:", mean_absolute_error(y_test_final, y_test_naive))
# print("R²:", r2_score(y_test_final, y_test_naive))


# --- Final Model B: Test Results ---
# MSE: 0.7108549019825634
# RMSE: 0.8431221157000707
# MAE: 0.4525773471733988
# R²: 0.3387848755005769

# --- Naive Forecast: Test Results ---
# MSE: 0.9087409703133819
# RMSE: 0.953279062139404
# MAE: 0.4932754727728412
# R²: 0.15471740836609116

# RMSE fell quite a bit which is a great sign. R^2 also fell, however this makes sense if the 
# test dataset did not have that much price variation



'''
Final Visualization: Actual vs Predicted Prices
'''
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))

# Actual Henry Hub prices
plt.plot(
    test_df["Month_Year"],
    y_test_final,
    label="Actual Henry Hub Price",
    linewidth=2
)

# Model B predictions
plt.plot(
    test_df["Month_Year"],
    y_test_pred,
    label="Model B Predictions",
    linewidth=2,
    linestyle="--"
)

# Naive baseline
plt.plot(
    test_df["Month_Year"],
    y_test_naive,
    label="Naive Forecast",
    linewidth=1.5,
    linestyle=":"
)

plt.title("Henry Hub Natural Gas Prices: Actual vs Predicted")
plt.xlabel("Month")
plt.ylabel("Price (USD/MMBtu)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

plt.show()
