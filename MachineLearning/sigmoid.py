import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
from sklearn.model_selection import train_test_split

#sigmoid function 
def sigmoid(z):
    return 1/(1+np.exp(-z))


#generate values for z

z= np.linspace(-10,10,100)
y = sigmoid(z)

#plot sigmoid function
plt.plot(z,y)
plt.title("sigmoid function")
plt.xlabel("z")
plt.ylabel("sigmoid(z)")
plt.grid()
plt.show()

#why we use sigmoid function in logistic regression
#sigmoid function maps any real-valued number into the (0,1)
#interval which can be interpreted as probability of belonging to a particular class.

