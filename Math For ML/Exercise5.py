# Python script: Probabilities for all distributions + Bayes

import numpy as np
from scipy.stats import bernoulli, binom, poisson, norm

print("=== 1. Bernoulli Distribution ===")
# Scenario: Coin toss, p(success=head)=0.6
p = 0.6
x_success = 1
x_failure = 0

P_success = bernoulli.pmf(x_success, p)
P_failure = bernoulli.pmf(x_failure, p)
print(f"P(Success=1) = {P_success}")
print(f"P(Failure=0) = {P_failure}\n")

print("=== 2. Binomial Distribution ===")
# Scenario: Coin tossed 5 times, probability of head=0.5, exactly 3 heads
n = 5
k = 3
p_head = 0.5

P_3_heads = binom.pmf(k, n, p_head)
print(f"P(3 heads in 5 tosses) = {P_3_heads}\n")

print("=== 3. Poisson Distribution ===")
# Scenario: 4 calls per minute on average, probability of 2 calls
lam = 4
k_calls = 2

P_2_calls = poisson.pmf(k_calls, lam)
print(f"P(2 calls in a minute) = {P_2_calls}\n")

print("=== 4. Gaussian (Normal) Distribution ===")
# Scenario: Exam scores, mu=70, sigma=10, probability X<80
mu = 70
sigma = 10
X = 80

P_less_80 = norm.cdf(X, loc=mu, scale=sigma)
print(f"P(Score < 80) = {P_less_80}")

# Probability X>80
P_greater_80 = 1 - P_less_80
print(f"P(Score > 80) = {P_greater_80}")

# Probability 60 < X < 80
P_between_60_80 = norm.cdf(80, loc=mu, scale=sigma) - norm.cdf(60, loc=mu, scale=sigma)
print(f"P(60 < Score < 80) = {P_between_60_80}\n")

print("=== 5. Bayes Theorem Example ===")
# Scenario: Disease testing
# P(Disease) = 0.01, P(Positive|Disease) = 0.99, P(Positive|NoDisease) = 0.05
P_disease = 0.01
P_no_disease = 0.99
P_pos_given_disease = 0.99
P_pos_given_no_disease = 0.05

# Total probability of positive
P_positive = P_pos_given_disease * P_disease + P_pos_given_no_disease * P_no_disease

# Bayes theorem: P(Disease|Positive)
P_disease_given_positive = (P_pos_given_disease * P_disease) / P_positive
print(f"P(Disease | Positive test) = {P_disease_given_positive}")