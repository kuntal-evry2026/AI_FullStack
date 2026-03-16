import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

columns = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "species"
]

df = pd.read_csv(url,header=None , names= columns)

#sample statictic 

# mean = df.mean(numeric_only=True)
# print(mean)

# std = df.std(numeric_only=True)
# print(df)

#sampleing

sample = df["sepal_length"].sample(30, random_state=42)

#sample statistic

mean = sample.mean()
std = sample.std()
n = len(sample)

#confidence interval

z_value = norm.ppf(0.975)
margin_of_error = z_value * (std/np.sqrt(n))
ci = (mean - margin_of_error , mean+ margin_of_error )

print("sample mean " , mean)

print("95% confidence interval : " ,ci)

