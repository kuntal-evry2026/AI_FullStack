from sklearn.linear_model import LinearRegression
import numpy as np 

#data 

x = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([2,4,6,8,10])

#model
model = LinearRegression()
model.fit(x,y)

#prediction
y_pred = model.predict(x)
print("predicted values :" ,y_pred)

#R square value

r2 = model.score(x,y)
print("R square value :" ,r2)

#coefficient
coef = model.coef_
print("Coefficient :" ,coef)

#intercept
intercept = model.intercept_
print("intercept :" ,intercept)

