import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

# Discrete Random Variable: Dice Roll
outcomes = [1, 2, 3, 4, 5, 6]  # Use 6 for a real die
probabilities = [1/6]*6

plt.bar(outcomes, probabilities, color="blue", alpha=0.7)  # <-- corrected here
plt.title("PMF of a Dice Roll")
plt.xlabel("Outcomes")
plt.ylabel("Probability")
plt.show()

# Continuous Random Variable: Uniform Distribution
x = np.linspace(0, 1, 100)
pdf = uniform.pdf(x, loc=0, scale=1)

plt.plot(x, pdf, color="red")
plt.title("PDF of Uniform (0,1)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()