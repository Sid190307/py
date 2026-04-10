1.	Create Series from List.
Code:
import pandas as pd

data = [1, 2, 3, 4, 5]
s = pd.Series(data)

print(s)

2.	Create Series with Custom Index
Code:
import pandas as pd

data = [10, 20, 30]
s = pd.Series(data, index=['A',  'B', 'C'])

print(s)

3.	Create a Series from Dictionary & perform Indexing operations.
Code:
import pandas as pd

data= {
    "Sujal": 85,
    "Rani": 60,
    "Mahesh": 75,
    "Soham": 95,
    "Supriya":60,
    "Anita":50
}
marks = pd.Series(data)

print(marks)

4.	Create a Series using the following data for creating a series
data = {
	"Sujal": 85,
	"Rani": 60,
	"Mahesh": 75,
	"Soham": 95,
	“Supriya”:60,
	“Anita”:50
}
a.	Access the data from the above dictionary
i.	Display the marks for the subject Soham
CODE:
import pandas as pd

data = {"Sujal":85, "Rani":60, "Mahesh":75, "Soham":95, "Supriya":60, "Anita":50}
s = pd.Series(data)
print("The created series\n")
print(s)

print("\nMarks for Soham")
for index, value in s.items():
    if index == "Soham":
        print(value)

i.	Print the third subject
CODE:
import pandas as pd

data = {"Sujal":85, "Rani":60, "Mahesh":75, "Soham":95, "Supriya":60, "Anita":50}
s = pd.Series(data)
print("The created series\n")
print(s)

print("\nMarks for Soham")
for index, value in s.items():
    if index == "Soham":
        print(value)

print("\nThe third subject")
i = 0
for index, value in s.items():
    i = i + 1
    if i==3:
        print(index)

a.	Perform filtering and arithmetic operations
CODE:
import pandas as pd

data = {"Sujal":85, "Rani":60, "Mahesh":75, "Soham":95, "Supriya":60, "Anita":50}
s = pd.Series(data)
print("The created series\n")
print(s)
    

print("\nStudents who scored more than 90")
for index, value in s.items():
    if value > 90:
        print(index)

print("\nStudents who scored less than 60")
for index, value in s.items():
    if value < 60:
        print(index)

print("\nAdding 5 marks to students who scored 50")
for index, value in s.items():
    if value == 50:
        s[index] = s[index] + 5
        print(index," = ", value)

print("\nAverage marks")
print(s.mean())

print("\nMaximum marks")
print(s.max())

print("\nMinimum marks")
print(s.min())


