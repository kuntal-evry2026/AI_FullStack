#Scenario Example (Medical Test)
#Suppose:
#1% of people have a disease
#
#A test detects the disease correctly 99% of the time
#
#The test has 5% false positives

#We want to find:

#If a person tests positive, what is the probability they actually have the disease?



# Given probabilities
P_disease = 0.01
P_no_disease = 0.99

P_pos_given_disease = 0.99
P_pos_given_no_disease = 0.05

# Calculate P(Positive)
P_positive = (P_pos_given_disease * P_disease) + (P_pos_given_no_disease * P_no_disease)

# Bayes theorem
P_disease_given_positive = (P_pos_given_disease * P_disease) / P_positive

print(P_disease_given_positive)


#output :-
#Even if the test is 99% accurate, the probability that a person actually has the disease after testing positive is only:

#≈ 16.7%


