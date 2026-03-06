import pandas as pd
import numpy as np

df_employees = pd.DataFrame({
    "emp_id": [101, 102, 103, 104, 105],
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "department_id": [1, 2, 1, 3, 4]
})

print("Employees DataFrame")
print(df_employees)


df_departments = pd.DataFrame({
    "department_id": [1, 2, 3, 5],
    "department_name": ["HR", "IT", "Finance", "Marketing"]
})

print("\nDepartments DataFrame")
print(df_departments)

#inner join
merged_inner = pd.merge(df_employees , df_departments , on="department_id", how="inner")

print("n\ninner join result :", merged_inner)