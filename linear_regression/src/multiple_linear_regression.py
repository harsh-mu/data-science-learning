import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, root_mean_squared_error, mean_absolute_error, r2_score
from statsmodels.api import add_constant
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Load Data
df = pd.read_csv('model_data/natural_gas_monthly_model_ready.csv')

# Show columns
# print(df.columns)

'''

Creating the data subset

    - Right now, the dataset has multiple columns that are tracking similar types of features, such as weather, storage, production, etc.
    - In order to avoid multicollinearity, we want to make sure we are removing unneccessary columns or combining columns to create one big measure

'''

subset_df = df[['henry_hub_price_usd_per_mmbtu', 
                'Month_Year',
                'natural_gas_total_consumption_mmcf', 
                'dry_natural_gas_production_mmcf', 
                'storage_weekly_lower_48_states_natural_gas_working_underground_storage_billion_cubic_feet', 
                'weather_heating_degree_days_united_states']].copy()
subset_df['Month_Year'] = pd.to_datetime(subset_df['Month_Year'])
subset_df = subset_df.sort_values(by='Month_Year', ascending = True).reset_index(drop=True)

# print(subset_df.head(10))
# print(subset_df.isna().sum())

# Splitting train/validation/test data
train_end = int(len(subset_df) * 0.6)
val_end = int(len(subset_df) * 0.8)
train_df = subset_df.iloc[:train_end].copy()
val_df = subset_df.iloc[train_end:val_end].copy()
test_df = subset_df.iloc[val_end::].copy()

target = 'henry_hub_price_usd_per_mmbtu'
features = ['natural_gas_total_consumption_mmcf', 
                'dry_natural_gas_production_mmcf', 
                'storage_weekly_lower_48_states_natural_gas_working_underground_storage_billion_cubic_feet', 
                'weather_heating_degree_days_united_states']

X_train = train_df[features]
y_train = train_df[target]

X_val = val_df[features]
y_val = val_df[target]

X_test = test_df[features]
y_test = test_df[target]


# Training
model = linear_model.LinearRegression()
model.fit(X_train, y_train)
intercept = model.intercept_
coefficient = model.coef_

# print(f"Intercept: {intercept}")
# print(pd.Series(model.coef_, index=features))

# Validation
y_val_pred = model.predict(X_val)

mse = mean_squared_error(y_val, y_val_pred)
rmse = root_mean_squared_error(y_val, y_val_pred)
mae = mean_absolute_error(y_val, y_val_pred)
r_squared = r2_score(y_val, y_val_pred)

# print(f"MSE: {mse}")
# print(f"RMSE: {rmse}")
# print(f"MAE: {mae}")
# print(f"R^2: {r_squared}")

'''
Model Performed quite poorly:
    - MSE: 7.383720619541284
    - RMSE: 2.7173002446438055
    - MAE: 1.9397923679442228
    - R^2: -0.7921018992188407

Now to figure out if multicollinearity is responsible
'''

corr = X_train.corr()
corr.index = ['Consumption', 'Production', 'Storage', 'HDD']
corr.columns = corr.index

# print(corr.round(3).to_string())

X_vif = add_constant(X_train)

vif = pd.Series(
    [
        variance_inflation_factor(X_vif.values, i)
        for i in range(1, X_vif.shape[1])
    ],
    index=X_train.columns,
    name='VIF'
)

# print(vif.round(2))

'''
Consumption and Heating Degree Days shows a overlap with the other predictors, so retry with a reduced model

VIF Results:
natural_gas_total_consumption_mmcf                                                           7.41
dry_natural_gas_production_mmcf                                                              2.23
storage_weekly_lower_48_states_natural_gas_working_underground_storage_billion_cubic_feet    1.07
weather_heating_degree_days_united_states                                                    6.82

'''

reduced_features = [feature for feature in features if feature != 'weather_heating_degree_days_united_states']
X_train_reduced = train_df[reduced_features]
X_val_reduced = val_df[reduced_features]

reduced_model = linear_model.LinearRegression()

reduced_model.fit(X_train_reduced, y_train)
y_val_pred_reduced = reduced_model.predict(X_val_reduced)

reduced_mse = mean_squared_error(y_val, y_val_pred_reduced)
reduced_rmse = root_mean_squared_error(y_val, y_val_pred_reduced)
reduced_mae = mean_absolute_error(y_val, y_val_pred_reduced)
reduced_r_squared = r2_score(y_val, y_val_pred_reduced)

# print(f"Reduced MSE: {reduced_mse}")
# print(f"Reduced RMSE: {reduced_rmse}")
# print(f"Reduced MAE: {reduced_mae}")
# print(f"Reduced R^2: {reduced_r_squared}")

# Retest VIF
X_vif_reduced = add_constant(X_train_reduced)

vif_reduced = pd.Series(
    [
        variance_inflation_factor(X_vif_reduced.values, i)
        for i in range(1, X_vif_reduced.shape[1])
    ],
    index=X_train_reduced.columns,
    name='VIF'
)

print(vif_reduced.round(2))

''' 
Results of removing Heating Degree Days:
    - Removing this column helped a lot with reducing collinearity
        - natural_gas_total_consumption_mmcf                                                           1.18
        - dry_natural_gas_production_mmcf                                                              1.10
        - storage_weekly_lower_48_states_natural_gas_working_underground_storage_billion_cubic_feet    1.07   

But it hurt RMSE from 2.717 with HDD to 2.724 without, therefore less predictor overlap makes individual coefficients easier to 
estimate, but does not guarantee better predictions
'''

# Investigate predictor overlap and compare a model without HDD.
y_test_pred = model.predict(X_test)

mse_test = mean_squared_error(y_test, y_test_pred)
rmse_test = root_mean_squared_error(y_test, y_test_pred)
mae_test = mean_absolute_error(y_test, y_test_pred)
r_squared_test = r2_score(y_test, y_test_pred)

print(f"Test MSE: {mse_test}")
print(f"Test RMSE: {rmse_test}")
print(f"Test MAE: {mae_test}")
print(f"Test R^2: {r_squared_test}")




'''
Summary:
    - Built a four-feature multiple linear regression for same-month
    Henry Hub price using consumption, production, storage, and HDD.
    - Used a chronological 60% training / 20% validation / 20% test split.
    - Consumption and HDD had strong correlation (0.838).
    - Their original VIF values were 7.41 and 6.82.
    - Removing HDD reduced all remaining VIF values to approximately 1.
    - However, validation RMSE increased slightly from 2.717 to 2.724.
    - Retained the four-feature model because it performed slightly better
    on validation data.

Main lesson:
Reducing multicollinearity does not guarantee better predictions.
VIF measures predictor redundancy; validation metrics measure
performance on unseen observations.

Limitations:
    - Both candidate models performed poorly on validation data.
    - This analysis models same-month relationships, not an advance forecast.
    - Seasonality, lagged effects, and changing relationships over time
    remain topics for future builds.
'''