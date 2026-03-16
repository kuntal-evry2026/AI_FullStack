# url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
import numpy as np 
from sklearn.linear_model import LinearRegression
#chi square test
from scipy.stats import chi2_contingency


#load data 

data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
print(data.head())
# #delete column 
# data = data.drop("sex", axis=1)
# data = data.drop("smoker", axis=1)
# data = data.drop("day", axis=1)
# data = data.drop("time", axis=1)
# #EDA
# sns.scatterplot (x="total_bill" , y = "tip" , data = data )
# plt.show()

# #corelation heatmap 
# sns.heatmap(data.corr() , annot = True)
# plt.show()

#hypothesis test 
#we want to see if there is a significant diffenece in tips

# male = data [data["sex"]=="Male"]["tip"]
# female = data [data["sex"]== "Female"]["tip"]

# t_stat , p_value = ttest_ind(male , female) 

# print("t stat :" , t_stat)
# print("p value :" , p_value)

# alpha = 0.05

# if p_value <alpha:
#     print("reject null hypothesis : there is a significant diff")
# else :
#     print("fail to reject null hypothesis : there is no significant diff")



#Liner regrssion 

x = data [["total_bill"]].values.reshape(-1, 1)
y = data ["tip"]

model = LinearRegression()
model.fit(x,y)

y_pred = model.predict(x)
print("predicted values :" , y_pred)

#R square value
r2 = model.score(x,y)
print ("R square value :" ,r2)

#coefficient
coef = model.coef_
print("coefficient :" ,coef)

#intercept
intercept = model.intercept_
print ("intercept :" ,intercept)

#output interpret the result

print("for every 1 unit increase in total bill , the tip increassed by :",coef[0])

#plt regression line

sns.scatterplot(x="total_bill" , y ="tip" , data=data)
plt.plot(x,y_pred ,color ="red")
plt.show()


#chi square test of independence
#we want to see if there is a sih=gnificance association betwwen sex and smoker

contigemcy_table = pd.crosstab(data["sex"],data["smoker"])
print(contigemcy_table)

stat,p_value ,dof , excepted  = chi2_contingency(contigemcy_table)
print("chi square stat :" ,stat)
print ("chi square p value :" ,p_value)
print("chi square dof :" ,dof)

alpha = 0.05

if p_value < alpha :
    print("reject null hypothesus : there is a significant association between sex and smoker")
else :
    print("fail to reject null hypothesis : there is no significance assocuation between sex and smoker")