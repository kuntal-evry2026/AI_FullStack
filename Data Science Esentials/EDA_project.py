#https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

#inspect data
print(df.describe())
print(df.info())

#Handle Missing Value 

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

#Remove duplicate
df = df.drop_duplicates()

#show first 5 data

print(df.head())

#Filter data : Passengers in  first class

first_class = df[df["Pclass"]==1]
print("first class passenges",first_class.head())


#Bar chart :survival rate by class

survival_by_class = df.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind="bar",color = "skyblue")
plt.title("survival rate by class")
plt.ylabel("survival rate")
plt.show()



#Histogram age distribution
sb.histplot(df["Age"],kde= True, bins=20 , color= "red")
plt.title("Age distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


#scatter plot age vs fare

plt.scatter(df["Age"],df["Fare"],alpha=0.5,color= "yellow")
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()