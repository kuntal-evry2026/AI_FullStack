import numpy as np
from scipy.stats import ttest_ind

#sample dataset 

group1 = [2.1,2.2,2.3,2.4,3.0,3.2]
group2 = [1.8,2.7,2.0,2.4,2.9,4.0]

#perform t test

t_stat , p_value = ttest_ind(group1,group2)

print("T-statistic :" ,t_stat)
print(" p- value :" ,p_value)


#interpetsation

alpha = 0.05

if p_value < alpha :
    print(" reject null hypothesis significant diffence")
else :
    print("fail to reject the null hypothesis : no significant diff")    