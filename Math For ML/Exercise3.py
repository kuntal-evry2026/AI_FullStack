import numpy as np 

# Define the gradient descent function

def gradient_descent (x,y, theta , learning_rate , iterations) :
    m = len(y)
    for _ in range (iterations):
        predictions = np.dot(x,theta)
        errors = predictions - y
        gradients = (1/m) * np.dot (x.T , errors)
        theta -= learning_rate * gradients
    return theta;    
    
# Sample Data (Linear relationship y = 2x + 1)
X = np.array([1,2,3,4,5])

y = np.array([3,5,7,9,11])

# Add bias column (intercept)
X = np.c_[np.ones(len(X)), X]

# Initial theta values
theta = np.zeros(2)

# Parameters
learning_rate = 0.01
iterations = 1000

# Run Gradient Descent
theta_final = gradient_descent(X, y, theta, learning_rate, iterations)

print("Final theta:", theta_final)    