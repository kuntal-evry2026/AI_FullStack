import numpy as np 
from scipy.stats import chi2_contingency
#Annova
from scipy.stats import f_oneway


d1 = np.array([[10,20],
              [20,30]])

stat , p , dof , expected = chi2_contingency(d1)

print(stat)
print(p)
print(dof)
print(expected)

#condition to reject null hypothesis 

alpha = 0.05

if p <alpha :
    print("Reject null hypothesis")
else :
    print("Fail to reject null hypothesis")
    
    
    
#Annova     

g1 = np.array([10,20,30,40,50])
g2= np.array ([100,200,300,400,500])
g3 = np.array([1000,2000,3000,4000,5000])


f_stat , p_value  = f_oneway(g1,g2,g3)

print(f_stat)
print (p_value) 