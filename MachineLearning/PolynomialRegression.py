import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score
from sklearn.model_selection import train_test_split

#generate synthetic data 

x= np.random.rand(100,1)*10
y = 0.5 * x**2 + 2*x + 3 + np.random.randn(100,1)*10

#split data into train and test 
x_train ,x_test ,y_train ,y_test = train_test_split(x,y,test_size=0.2 , random_state= 42)

#ploynomial features
poly = PolynomialFeatures(degree=2)
x_train_poly = poly.fit_transform(x_train)
x_test_poly = poly.transform(x_test)

#train the model
model = LinearRegression()
model.fit(x_train_poly ,y_train)

#prediction
y_pred = model.predict(x_test_poly)

#evaluate the model 

mse  = mean_squared_error(y_test , y_pred)

r2 = r2_score(y_test ,y_pred)

print("Mean squared error :" , mse)

#visualization

plt.scatter(x_test,y_test , color  = "blue" ,label = "Actual")
plt.scatter(x_test , y_pred ,color = "red" , label = "predicted")
plt.show()

