import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge , Lasso
#fetching data 
from sklearn.datasets import fetch_california_housing

# ================================
# LOAD DATA
# ================================
data = fetch_california_housing(as_frame=True)
df = data.frame

# Feature and target
X = df[["MedInc"]].values      # convert to numpy ✅
y = df["MedHouseVal"].values   # 1D array ✅


# ================================
# POLYNOMIAL TRANSFORMATION
# ================================
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# #Fit polynomial regression model 

# model = LinearRegression()
# model.fit(x_poly ,y)

# #make prediction
# y_pred = model.predict(x_poly)


# #plot actual vs predicted values

# plt.figure(figsize=(10, 6))
# plt.scatter(y, y_pred, alpha=0.5)
# plt.xlabel("Actual Values")
# plt.ylabel("Predicted Values")
# plt.title("Actual vs Predicted Values")
# plt.show()

# #evaluate the model 

# mse  = mean_squared_error(y , y_pred)
# print("Mean square error :" ,mse)









# ================================
# TRAIN-TEST SPLIT (FIXED ✅)
# ================================
X_train, X_test, y_train, y_test = train_test_split(
    X_poly, y,
    test_size=0.2,
    random_state=42
)


# ================================
# RIDGE MODEL
# ================================
ridge = Ridge(alpha=0.1)
ridge.fit(X_train, y_train)

y_pred_ridge = ridge.predict(X_test)

mse_ridge = mean_squared_error(y_test, y_pred_ridge)
print("Ridge MSE:", mse_ridge)


# ================================
# LASSO MODEL
# ================================
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

y_pred_lasso = lasso.predict(X_test)

mse_lasso = mean_squared_error(y_test, y_pred_lasso)
print("Lasso MSE:", mse_lasso)


# ================================
# VISUALIZATION (FIXED ✅)
# ================================

# IMPORTANT: use only original feature for plotting
# (first column = MedInc)
X_test_1D = X_test[:, 0]

# sort for smooth curve
sorted_idx = np.argsort(X_test_1D)

X_sorted = X_test_1D[sorted_idx]
y_sorted = y_test[sorted_idx]
ridge_sorted = y_pred_ridge[sorted_idx]
lasso_sorted = y_pred_lasso[sorted_idx]

# plot
plt.figure(figsize=(10, 6))

# actual data
plt.scatter(X_test_1D, y_test, color="blue", alpha=0.5, label="Actual")

# ridge curve
plt.plot(X_sorted, ridge_sorted, color="red", linewidth=2, label="Ridge")

# lasso curve
plt.plot(X_sorted, lasso_sorted, color="green", linestyle="--", linewidth=2, label="Lasso")

plt.xlabel("Median Income")
plt.ylabel("Median House Value")
plt.title("Ridge vs Lasso Regression (Polynomial)")

plt.legend()
plt.show()