import numpy as np
import matplotlib.pyplot as plt

# Average number of events
lam = 5

# Number of experiments
size = 1000

# Generate Poisson distributed data
data = np.random.poisson(lam, size)

# Plot histogram
plt.hist(data, bins=15, edgecolor='black')

plt.title("Poisson Distribution")
plt.xlabel("Number of Events")
plt.ylabel("Frequency")

plt.show()