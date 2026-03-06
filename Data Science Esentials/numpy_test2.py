import numpy as np

np.random.seed(28)

# crate a array 

arr = np.array([1,2,3,4,5])
print(arr+10)

matrix = np.array([[1,2,3],[4,5,6]])
vector = np.array([7,8,9])
print(matrix+vector)

print("sum",np.sum(matrix))
print("subtract",np.subtract(matrix,vector))
print("min",np.min(matrix))
print("max",np.max(matrix))
print("mean",np.mean(matrix))
print("standard devision",np.std(matrix))
print("median",np.median(matrix))
print("columnz",np.sum(matrix,axis =0))
print("rows",np.sum(matrix,axis =1))


#create random array

random_Arr = np.random.rand(3,4)
print(random_Arr)

random_int = np.random.randint(0,10,(3,4))
print(random_int)