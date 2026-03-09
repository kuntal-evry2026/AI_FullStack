import numpy as np
import matplotlib.pyplot as plt

# Probability of success
p = 0.7

# Number of trials
n = 1000

# Generate Bernoulli distributed data
data = np.random.binomial(1, p, n)

# Plot histogram
plt.hist(data, bins=2, edgecolor='black')

plt.title("Bernoulli Distribution")
plt.xlabel("Outcome (0 = Failure, 1 = Success)")
plt.ylabel("Frequency")

plt.show()