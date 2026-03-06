import numpy as np 

# creating random data integer 

random_init = np.random.randint(0,10,(3,4))
print(random_init)

#filter 

filter_Arr = random_init[random_init>5]=0
print(filter_Arr)

print(random_init.mean())
print(random_init.std())