1.	Create a DataFrame from a list.
CODE:
import pandas as pd

data = [10,20,30,40]
s = pd.DataFrame(data)
print(s)

2.	Create a DataFrame from a list of lists.
CODE:
import pandas as pd

data = [ ['Alex',20], ['john',45], ['Mahesh',60] ]
d = pd.DataFrame(data, columns=['Name','Age'])
print(d)

3.	Create a DataFrame from a dictionary of lists.
CODE:
import pandas as pd

data = {'Name': ['Sajiv', 'Rishabh', 'Ashish', 'Neel'], 'Age': [18,19,17,18] }
d = pd.DataFrame(data)
print(d)

4.	Create a DataFrame from a list of dictionaries.
CODE:
import pandas as pd

data = [{'a': 1, 'b': 2}, {'a':10, 'b':20, 'c':30}]
d = pd.DataFrame(data)
print(d)

5.	Create DataFrame from dictionaries of series.
CODE:
import pandas as pd

data = {'one': pd.Series([1,2,3], index=['a','b','c']),
        'two': pd.Series([1,2,3,4], index =['a','b','c','d']) }
d = pd.DataFrame(data)
print(d)

6.	Create a DataFrame using the following data:
    import pandas as pd
	
	data ={ "Roll no": [101, 102, 103, 104, 105],  "Name": ["Amit","Soham","Neha","Rahul", "Ajay"], "Marks": [80,95,60,70,75] }
	d = pd.DataFrame(data)
	print(d)

        print("\nAdding a new column grade")
	d['Grade'] = ["A", "A+", "B", "B", "C"]
	print(d)
	
	print("\nFirst three rows of the dataframe")
	print(d.iloc[:3, :])
	
	print("\nLast three rows of the dataframe")
	print(d.iloc[-3:, :])
	
	print("\nThe column labels of the dataframe")
	print(d.columns)
	
	print("\nTwo columns of the dataframe")
	print(d.loc[ :, 'Name': 'Marks'])
	
	print("\nRename the column “Name” by “Student Name”")
	d = d.rename(columns={'Name': 'Student Name'})
	print(d)

	print("\nChange the Name “Neha” to “Rekha”")
	d.replace({'Student Name':"Neha"}, "Rekha", inplace=True)
	print(d)
	
	print("\nRemove the student who has scored 60 marks")
	result = d[ d["Marks"] != 60]
	print(result)

