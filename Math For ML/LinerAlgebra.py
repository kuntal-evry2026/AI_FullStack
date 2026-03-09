import numpy as np 

A = np.array([[1,2] , [3,4]])
B = np.array([[5,6],[7,8]])

print("Addition \n ",A+B)
print("Subtraction \n",A-B)

C = A *2

print("Scaler Multiplication \n" , C)

result = np.dot(A,B)
print (" Matrix Multipilication \n" , result)


#special matrix

I = np.eye(3)
print("Identify Matrix \n" , I)


#zero matrix

z= np.zeros((2,3))
print("Zero Matrix \n" ,z)


#Diagonal Matrix

D= np.diag([2,3])

print("Diagonal Matrix \n" ,D )



