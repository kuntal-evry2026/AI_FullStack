import pandas as pd
from scipy.stats import skew , kurtosis
import seaborn as sns
import matplotlib.pyplot as plt

df = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

columns = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "species"
]

df = pd.read_csv(df, header=None, names=columns)

#Analyze sepal_length

feature = df ["sepal_length"]
print("skewness :" ,skew(feature))
print("Kurtosis" ,kurtosis (feature))


#visual distribution
sns.histplot(feature , kde=True)
plt.title("Distribution of sepal length")
plt.show ()




