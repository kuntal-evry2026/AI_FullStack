import pandas as pd

s = pd.Series([1,2,3,4], index = ['a','b','c','d'])
print(s)


data = {'name ': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)


df = pd.read_csv('data.csv')
df.to_csv('output.csv',index = False) #store data in csv file
df = pd.read_excel('data.xlsx')


#viewing data
print(df.head()) #first 5 rows
print(df.tail()) #last 5 rows

print(df.info()) #summary of the dataframe
print(df.describe()) #statistical summary of numerical columns

print(df['age']) #accesing a column
print(df[df['age']>30]) #validation of data through condition

print(df.iloc[0]) #accesing first row

