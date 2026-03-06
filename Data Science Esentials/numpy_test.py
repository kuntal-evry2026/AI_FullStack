import numpy as np 
arr = np.array([1,2,3,4,5])
print(arr)

zeros = np.zeros((3,4))
print(zeros)

ones = np.ones((2,3))
print(ones)

range = np.arange(0,10,2)
print(range)

arr1 = np.array([1,2,3,4,5,6])
arr1reshaped = arr1.reshape(2,3)
print(arr1reshaped)

arr2 = np.array([1,2,3])
expanded_arr2 = arr2[:,np.newaxis]
print(expanded_arr2)

a= np.array([1,2,3])
b= np.array([4,5,6])
c= a+b
print(c)
sqrt = np.sqrt(c)
print(np.sum(sqrt))
print(np.min(sqrt))
print(np.max(sqrt))
print(sqrt[1])
print(sqrt[-1])


Matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(Matrix)

#Transpose

Transpone = Matrix.T
print(Transpone)