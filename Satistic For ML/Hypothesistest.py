import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from scipy.stats import ttest_1samp

#sample data 

data = [12,14,35,46,78,90]

#null_ Hypothesis 

mean = np.mean(data)
print("mean :" ,mean)

#perform t-test 
t_stat , p_value = ttest_1samp(data,mean)
print("T-statistics :" ,t_stat)
print("P-value :" ,p_value)


#interpret the result 
alpha = 0.05

if p_value <=alpha :
    print ("Reject the null hypothesis : significant difference ")
else :
    print    ("Fail to reject the null hypthesis : no significant differnce")
    
    