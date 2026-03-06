df = df.dropna() #drop missing values
df = df.fillna(df.mean()) #fill missing value with mean of the colomn

df ["column_name"] = df ["column_name"].fillna(0) #fill missing value with 0

df.fillna(mathod ="ffill") #fill missing value with forward fill

df.fillna(method = "bfill") #fill missing value with backword fill

df["column_name"] = df["column_name"].interpolate() #fill missing value with interpolation

df = df.rename (columns = {"old_name":"new_name"}) #rename columns 

df["column_name"] = df["column_name"].astype(int) #change data type of a column to int

df["new_column"] = df["existing_column"]*2 #create new column by performing operateion

combined_df = pd.concat([df1 , df2],axis = 0 ) # combine two dataframes vertically

combined_df = pd.concat([df1 , df2],axis = 1 ) # combine two dataframes horizantaly

merged_df =pd.merge(df1 ,df2 ,on = "common_column") #merge two dataframes based on common column

merged_df = pd.merge(df1, df2, on = "common_column" , how = "inner") #inner join


merged_df = pd.merge(df1, df2, on = "common_column" , how = "outer") #outer join



merged_df = pd.merge(df1, df2, on = "common_column" , how = "left") #left join

joined_df = df1.join(df2 ,how = "index") #join two dataframes based on index

