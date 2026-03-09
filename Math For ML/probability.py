#def bayes_theorem (prior , likelihood , evedence) :
#    return likelihood*prior / evedence


import numpy as np
import matplotlib.pyplot as plt

# Parameters of Gaussian distribution
mean = 0
std_dev = 1
size = 1000

# Generate random numbers from Gaussian distribution
data = np.random.normal(mean, std_dev, size)

# Plot histogram
plt.hist(data, bins=30, density=True, alpha=0.6, color='blue')

# Create x values for Gaussian curve
x = np.linspace(min(data), max(data), 100)

# Gaussian function
y = (1/(std_dev*np.sqrt(2*np.pi))) * np.exp(-(x-mean)**2/(2*std_dev**2))

# Plot Gaussian curve
plt.plot(x, y, color='red')

plt.title("Gaussian Distribution")
plt.xlabel("Value")
plt.ylabel("Probability Density")

plt.show()