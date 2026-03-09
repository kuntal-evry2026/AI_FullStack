import numpy as np

# Task 1: Implement the mathematical formula for Linear Regression
def predict(X, theta):
    return np.dot(X, theta)


# Task 2: Use Gradient Descent to optimize model parameters
def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)

    for _ in range(iterations):
        gradients = (1/m) * np.dot(X.T, (np.dot(X, theta) - y))
        theta = theta - learning_rate * gradients

    return theta


# Task 3: Calculate evaluation metrics

def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def r_squared(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - (ss_res / ss_tot)



# Sample dataset
X = np.array([[1,1], [1,2], [1,3], [1,4]])
y = np.array([2,4,6,8])

theta = np.zeros(X.shape[1])

# Train model
theta = gradient_descent(X, y, theta, learning_rate=0.01, iterations=1000)

# Predictions
y_pred = predict(X, theta)

# Metrics
print("Theta:", theta)
print("MSE:", mean_squared_error(y, y_pred))
print("R²:", r_squared(y, y_pred))