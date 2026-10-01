import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('model_data/natural_gas_monthly_model_ready.csv')

''' Data Exploration '''
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# print(df.isna().sum())


''' Correlation Analysis '''
prices_series = df["henry_hub_price_usd_per_mmbtu"]
correlation_df = df.drop(columns=["henry_hub_price_usd_per_mmbtu"])

for column in correlation_df.columns:
    if correlation_df[column].dtype != 'object':
        correlation = prices_series.corr(correlation_df[column])
        # print(f"Correlation between henry_hub_price_usd_per_mmbtu and {column}: {correlation}")

''' Data Visualization '''
# plt.title('Storage vs Henry Hub Price')
# plt.scatter(df['storage_weekly_salt_south_central_region_natural_gas_working_underground_storage_billion_cubic_feet'], 
#             df['henry_hub_price_usd_per_mmbtu'])
# plt.xlabel('Storage (Billion Cubic Feet)')
# plt.ylabel('Henry Hub Price (USD per MMBtu)')
# plt.show()

''' Simple Regression '''
from sklearn import linear_model
from sklearn.model_selection import train_test_split

# Split training/testing data
y = df['henry_hub_price_usd_per_mmbtu']
X = df[['storage_weekly_salt_south_central_region_natural_gas_working_underground_storage_billion_cubic_feet']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Fitting model
model = linear_model.LinearRegression()
model.fit(X_train, y_train)
intercept = model.intercept_
coefficient = model.coef_

# print(f"Intercept: {intercept}")
# print(f"Coefficient: {coefficient}")

# Find prediction
y_pred = model.predict(X_test)

# Find MSE, RMSE, MAE, R^2
from sklearn.metrics import mean_squared_error, root_mean_squared_error, mean_absolute_error, r2_score

mse = mean_squared_error(y_test, y_pred)
rmse = root_mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r_squared = r2_score(y_test, y_pred)

# print(f"mse: {mse}")
# print(f"rmse: {rmse}")
# print(f"mae: {mae}")
# print(f"r_squared: {r_squared}")

# Plotting residuals
residuals = list(y_test - y_pred)
plt.scatter(y_pred, residuals)
plt.xlabel("Predicted")
plt.ylabel("Residual")
plt.title("Residuals vs Predicted Scatter")
plt.axhline(0)
plt.show()



