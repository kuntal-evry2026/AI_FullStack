import  numpy as np
from scipy.stats import pearsonr , spearmanr


#pearson correalation 
x =np.array([1,2,3,45,5])
y= np.array([10,20,30,40,50])


r , p_value  = pearsonr(x,y)
print("pearson corelation :" ,r)

#spearman corelation 

roh , p_value = spearmanr(x,y)
print("spearman corelation :" ,roh)