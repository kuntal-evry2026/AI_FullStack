import numpy as np

#simulating 10,000 dice rolls 

rolls = np.random.randint(1,7,size=10000)

#calsulate probabilities

p_even = np.sum(rolls % 2 == 0) / len (rolls)
p_greater_than_4 = np.sum (rolls >4) /len(rolls)

print("p of even" , p_even)
print(" p of greater than 4" , p_greater_than_4)

