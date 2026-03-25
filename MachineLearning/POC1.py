import numpy as np  
import pandas as pd 
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score , classification_report
from sklearn.linear_model import LinearRegression
#import classification and logestic model 
from sklearn.linear_model import LogisticRegression
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn.metrics import mean_squared_error , mean_absolute_error



#load the data 

data = fetch_california_housing(as_frame=True)

df = data.frame

#define feature and target 

x= df[['MedInc' , 'HouseAge' ,'AveRooms' ]]
y= df['MedHouseVal']

#inspect data 

print(df.info())

print(df.describe())

print(df.head())

#visualize relationship 

sns.pairplot(df , vars=['MedInc' , 'HouseAge' ,'AveRooms' ,'MedHouseVal'])

plt.show()


#check for missing values 

print("Missing Values :\n", df.isnull().sum())


#split dataset 

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=42)

#train linear regression model 

model = LinearRegression()
model.fit(x_train,y_train)

#make prediction 
y_pred = model.predict(x_test)

#evaluate perfomance 

mse = mean_squared_error(y_test,y_pred)
mae = mean_absolute_error(y_test,y_pred)

#print result 

print("Mean squared error :" , mse)
print("Mean absolute error :" ,mae)


