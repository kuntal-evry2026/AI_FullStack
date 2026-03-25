#Define feature and target files 

import pandas as pd 

url ="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

data = pd.read_csv(url)

#feature and target value 

feature = data[["total_bill", "tip"]]
target = data["sex"]

print("feature :",feature.head())
print("target :" ,target.head())


#spliting data into train and test 

from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test  = train_test_split(feature , target , test_size=0.2 , random_state= 42)

print ("x_train :" , x_train.head())
print("y_train :" , y_train.head())

print("x_test :" , x_test.head())
print("y_test :" ,y_test.head())



#visualization 
import seaborn as sns 
import matplotlib.pyplot as plt


#relation between feature and target


sns.scatterplot(x="total_bill", y="tip", hue="sex", data=data)
plt.title("Relation between Total Bill and Tip")
plt.show()

