#different type of  Hypothesis test

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind ,ttest_rel ,ttest_1samp
from scipy.stats import ttest_rel
from scipy.stats import chi2_contingency
from scipy.stats import f_oneway

#1sample t test 
d8  = np.array([10,20,30,40,50])
population_mean =  sum(d8) / len(d8)
t_Stat , p_value = ttest_1samp(d8 , population_mean)
#independent t test 
#t tset = (mean1 - mean2) /sqrt((var1/n1)+(var2/n2))

#why we use t test when we have small sample size and we don't know the population standard deviation

d1 = np.array([100,200,345,678])
d2 = np.array([1,2,3,4])

t_stat , p_value = ttest_ind(d1 ,d2)

print(t_stat)
print(p_value)

#paired t test
d3 = np.array([100,456,764,892])
d4 = np.array ([200,567,895,903])

t_stat , p_value = ttest_rel(d3 ,d4)

#why we use paired t test when we have two related samples or matched samples

print("paired t test :" , t_stat)
print("paird t_test p value :" , p_value)



# chi square test of independence 
#why we use chi square test of independence when we have two categorical variables and we want to see if they are independent or not

p_value , stat , dof , expected  = chi2_contingency([[10,20],[30,40]])

print("Chi square test of independence :" ,stat)
print ("chi square test of independence p value :" , p_value)
print ("chi square test of independence dof :" ,dof)

#Annova test 

f_stat , p_value = f_oneway([10,20,30,40,50] , [100,200,300,400,500] , [1000,2000,3000,4000,5000])
print ("Annova test :" ,f_stat)
