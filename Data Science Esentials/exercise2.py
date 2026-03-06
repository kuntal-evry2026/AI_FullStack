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

print("column", df[["sepal_length"]])


print("first 5 rows",df.head())
print("last 5 rows",df.tail())
print("info",df.info())
print("summary",df.describe())
print("column ",df[["sepal_length"]])


filter_df = df[(df["sepal_length"]>5.0) & (df["species"]=="Iris-virginica")]
print("filter", filter_df)