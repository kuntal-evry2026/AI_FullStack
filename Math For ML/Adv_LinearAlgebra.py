import numpy as np

A = np.array([[1,2],
              [3,4]])

#Determinant
determinant = np.linalg.det(A)

print("Determinant:", determinant)


#inverse 

inverse = np.linalg.inv(A)

print("inverse:" ,inverse)


#Eigenvalue n Eigenvector

eigenvalues , eigenVectors = np.linalg.eig(A)

print("Eigenvalue \n" ,eigenvalues)
print(" Eigenvactor \n" , eigenVectors)


#Matrix Decomposition 

U, S, Vt = np.linalg.svd(A)

print("U matrix:\n",U)
print("Singular values:",S)
print("V transpose:\n",Vt)