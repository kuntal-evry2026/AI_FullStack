import numpy as np
import matplotlib.pyplot as plt

# Parameters
n = 10      # number of trials
p = 0.5     # probability of success
size = 1000 # number of experiments

# Generate binomial data
data = np.random.binomial(n, p, size)

# Plot histogram
plt.hist(data, bins=11, edgecolor='black')

plt.title("Binomial Distribution")
plt.xlabel("Number of Successes")
plt.ylabel("Frequency")

plt.show()