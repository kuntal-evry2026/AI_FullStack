import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb 
import pandas as pd

df = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

columns = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "species"
]

df = pd.read_csv(df, header=None, names=columns)
df = df.drop("species", axis=1)


corelation_Matrix = df.corr()

#plot heatmap 
sb.heatmap(corelation_Matrix , annot= True , cmap= "coolwarm")
plt.show()