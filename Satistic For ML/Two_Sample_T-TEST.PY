import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

#Data from two groups

group1 = np.array([5,7,8,9,0])
group2 = np.array([6,7,8,9,12])

#performing two sample t-test

t_statistic , p_value  = ttest_ind(group1,group2)

print("T-Statistic :" ,t_statistic)
print("P-Value :" ,p_value)


#visualization of the data 

plt.boxplot([group1,group2], labels = ['Group 1' ,'Group 2'])
plt.title('boxplot')
plt.show()

#condition to check the significant of the result

alpha = 0.05

if p_value < alpha :
    print ("Reject the null hypothesis , there is a significant difference between the two groups ")
    
else :
    print ("Fail to reject the null hypothesis , there is no significance diff two group")

