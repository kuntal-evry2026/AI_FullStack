import numpy as np

N = 10000

# 0 = Tails, 1 = Heads
tosses = np.random.randint(0, 2, N)

# probabilities
p_heads = np.mean(tosses == 1)
p_tails = np.mean(tosses == 0)

print("Probability of Heads:", p_heads)
print("Probability of Tails:", p_tails)