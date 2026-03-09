import scipy.stats as sp

data = [10,20,30,40,50]
mean = sum(data) / len(data)
sample_mean = mean

variance = sum ((x- mean) **2 for x in data) / len(data)
std_dev = variance ** 0.5

z_score =1.96

ci = (sample_mean - z_score * (std_dev / len(data) ** 0.5),
      sample_mean + z_score * (std_dev / len(data) ** 0.5)
      ) 
print("95% confidence interval :" ,ci)