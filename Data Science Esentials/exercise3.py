import pandas as pd
import numpy as np

#create a dataframe with missing value 

data = {
    "Name": ["Alice", "Bob", "Charlie", None],
    "Age": [25, np.nan, 35, 40],
    "Salary": [50000, 60000, None, 80000]
}

df = pd.DataFrame(data)

print(df)

#fill missing value fill with mean of the column
df_filled_mean = df.fillna(df.mean(numeric_only = True))
print("filled with mean" ,df_filled_mean)


#rename column

df_renamed = df.rename(columns={"Name":"Full Name"})
print(df_renamed)