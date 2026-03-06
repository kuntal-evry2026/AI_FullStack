import pandas as pd
data = {
    "Student_ID": [101,102,103,104,105,106,107,108,109,110],
    "Name": ["Aarav","Diya","Rohan","Anika","Kabir","Meera","Arjun","Sara","Vivaan","Isha"],
    "Age": [16,17,16,17,18,16,17,18,16,17],
    "Class": ["10A","10A","10B","10B","10A","10B","10A","10B","10A","10B"],
    "Math": [78,85,67,90,88,72,95,60,83,77],
    "Science": [82,79,74,91,86,70,89,65,80,76],
    "English": [75,88,69,85,90,73,92,68,81,79],
    "Attendance_Percent": [92,95,88,97,90,85,98,80,93,89]
    }
 
df = pd.DataFrame(data)
print(df)
 
grouped = df.groupby("Class").mean(numeric_only=True)
print(grouped) 

pivort =  df.pivot_table(index = "Class" , values = "Math" , aggfunc  = "mean")
print(pivort)
 