# Simulate 10,000 experiments of rolling two dice.

# Tasks:

# Compute probability of sum = 7

# Compute probability of sum > 10

# Compute probability of same numbers (doubles)


import numpy as np

# number of experiments
N = 10000

# simulate dice rolls
die1 = np.random.randint(1, 7, N)
die2 = np.random.randint(1, 7, N)

# sum of dice
sums = die1 + die2

# probabilities
p_sum_7 = np.mean(sums == 7)
p_sum_gt_10 = np.mean(sums > 10)
p_doubles = np.mean(die1 == die2)

print("P(sum = 7):", p_sum_7)
print("P(sum > 10):", p_sum_gt_10)
print("P(doubles):", p_doubles)