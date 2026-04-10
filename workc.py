Code:
#using csv files
"""
Display
- First 10 rows
- Last 10 rows
- Shape of dataset
- Column names
- Data types
- Summary statics
"""

import pandas as pd

df = pd.read_csv("students_marks.csv")

#print(df)

print("\nFirst 6 records - ")
print(df.head(6))

print("\nLast 6 records - ")
print(df.tail(6))

print("\nShape of Dataset:")
print (df.shape)

print ("\nColumn Names:")
print (df.columns)

print ("\nData Types:")
print (df.dtypes)

print ("\nSummary Statistics")
print (df.describe)


Selection & Filtering
Display:
import pandas as pd

df = pd.read_csv("students_marks.csv")


•	Name and Marks
Code:
print("\nName & Marks:")
print(df [[ "Name", "Marks"]])


•	Gender column
Code:
	print("\nGender column:")
print(df["Gender"])


•	Display students who scored more than 80 marks.
Code:
	print("\nStudents scoring more than 80 marks:")
print(df[df["Marks"] > 80])	


•	Display students who scored less than 40 marks.
Code:
print("\nstudents who scored less than 40 marks")
print(d[d["Marks"] < 40])


•	Count how many students scored below 50.
Code:
print("\nstudents scored below 50")
print(d[d["Marks"] < 50].shape[0])






