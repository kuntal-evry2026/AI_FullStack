import numpy as np

outcomes = np.array ([1,2,3,4,5,6])
probabilities = np.array([1/6]*6)
print(probabilities)


#expectation 

expectation = np.sum (outcomes*probabilities)
print("expectation mean :" , expectation)


#variance and standard devision 

variance = np.sum((outcomes -expectation) **2 *probabilities)
print ("variance :" ,variance)

std_dev = np.sqrt(variance)
print ("standard devision :" ,std_dev)