import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score

# generate random data

x = np.random.rand(100,1)*10
y = 2.5 * x + np.random.randn(100,1)*2

#split data into tran and tsst
x_train ,x_test ,y_train ,y_test = train_test_split(x,y,test_size=0.2 , random_state= 42)

#train the model
model  = LinearRegression()
model.fit(x_train ,y_train)

#prediction
y_pred = model.predict(x_test)

#evaluate the model 
mse = mean_squared_error(y_test ,y_pred)
r2  = r2_score(y_test ,y_pred)

print("Mean squared error :" ,mse)
print ("R2 score :" ,r2)

#visualization
plt.scatter(x_test ,y_test ,color = "blue" , label = "Actual")
plt.scatter (x_test ,y_pred ,color = "red" ,label = "Predicted")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Actual vs Predicted")
plt.legend()
plt.show()

#coefficent and intercept

coef = model.coef_[0][0]
intercept = model.intercept_[0]

print("slope (coefficient) :" ,coef)
print("intercept :" ,intercept)

#interpretation of coefficent and intercept
print("Interpretation of coefficient : For every unit increase in x , y increases by " ,coef)
print("Interpretation of intercept : When x is 0 , y is " ,intercept)
