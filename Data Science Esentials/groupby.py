groupes = df.groupby("column_name") #grouping data by column

for name , group in groupes : #iterating through groups
    print("group name " ,name)
    print("group data" , group)
    
    
    
groupes.mean()
groupes.sum()

df.groupby("column_name")["numeric_column"].mean() #groupin and calculating mean of a specific column

df.groupby("column_name").agg({"numeric_column1" : ["mean" , "max"]}) #grouping and applying multipile aggregation functions on different columns 

pivot = df.pivot_table(
    values = "numeric_column",
    index = "category_column",
    aggfunc = "mean"
) #creating pivot table to find mean of numeric column for each category in category column

def range_func(x):
    return x.max() - x.min()

df.groupby("column_name")["numeric_Column"].agg(range_func)


df.groupby("column_name")["numeric_Column"].mean()
df.groupby("column_name")["numeric_Column"].max()
df.groupby("column_name")["numeric_Column"].min()





