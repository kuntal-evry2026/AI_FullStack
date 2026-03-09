import numpy as np

#create matrics

A = np.array([[1,2],[3,4]])
B= np.array([[32,33],[78,90]])

#Addition
print("Addition :" , A+B)

#Subtraction
print("subtraction :" , B-A)

#Scaler mULTIPILCATION 
scaler = A*2
print ("Scaler Multiplicatio :",scaler )

#Multiplication 

C = np.dot(A,B)
print("Multiplication :" , C)