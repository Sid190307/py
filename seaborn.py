1.	Program to plot a simple scatter chart using the inbuilt dataset tips
Code:
“””
Program to plot a scatter chart using the inbuilt dataset tips
“””

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset ("tips")
print ("\nPrint first few records")
print(tips.head () )

sns.scatterplot (data=tips, x="total_bill", y="tip")

plt.show ()



2.	Program to plot a Scatter chart using Seaborn
Code:
“””
Program to plot a Scatter chart using Seaborn
“””

import seaborn as sb
import matplotlib.pyplot as mplt

df = sb.load dataset ("iris")

print ("\nFirst 5 records of iris dataset:")
print (df.head() )

mplt.figure(figsize=(10,5))

print ("\nExample without hue")
sb.scatterplot (
x="sepal_length",
y="petal_length",
data=df
)

##print ("\nExample with hue")
##sb. scatterplot (
## 	x = "sepal_length",
##	 y = "petal_length",
## 	hue = "species",
## 	data = df
##	)

mplt. title ("Sepal length vs Petal Length (Iris Dataset) ")
mplt.xlabel ("Sepal Length")
mplt.ylabel ("Petal Length")
mplt.grid (True)
mplt. show ()



3.	Program to generate a line plot using Seaborn’s inbuilt tips dataset. Average Total Bill per Day
Code:
“””
Generating a line plot using Seaborn's inbuilt tips dataset.
Average Total Bill per Day
“””

import seaborn as sb
import matplotlib.pyplot as mplt

df = sb.load_dataset ("tips")

print ("\nFirst 5 records of Tips Dataset:")
print (df.head () )

mplt.figure (figsize = (10,5))

sb.lineplot (
x = "day",
y = "total_bill",
data = df,
marker = "o"
)

mplt. title ("Average Total Bill per Day")
mplt.xlabel ("Day")
mplt.ylabel ("Total Bill")
mplt.grid ()
mplt. show ()


4.	Program to Generate a line plot using Seaborn’s inbuilt tips dataset. Grouped by  Gender.
Code:
“””
Generating a line plot using Seaborn's inbuilt tips dataset.
Grouped by Gender
“””

import seaborn as sb
import matplotlib.pyplot as mplt

df = sb.load_dataset ("tips")

print ("\nFirst 5 records of Tips Dataset:")
print (df.head())

mplt.figure (figsize = (10,5))

sb.lineplot(
x = "day",
y = "total bill",
hue = "sex",
data = df,
marker = "o"
)

mplt. title ("Average Total Bill per Day (Male vs Female) ")
mplt.xlabel ("Day")
mplt.ylabel ("Total Bill")
mplt.legend (title = "Gender")
mplt.grid()
mplt. show ()



5.	Program to Generate a line plot using Seaborn’s inbuilt tips dataset for the tips given by Smoker vs Non-Smoker customers
Code:
“””
Generating a line plot using Seaborn's inbuilt tips dataset.
Smoker vs Non-Smoker
“””

import seaborn as sb
import matplotlib.pyplot as mplt

df = sb.load_dataset ("tips")

print ("\nFirst 5 records of Tips Dataset:")
print (df.head () )

mplt.figure (figsize = (10,5))

sb.lineplot (
x = "day",
y = "tip",
hue = "smoker",
data = df,
marker = "o"
)

mplt.title ("Average Tip per Day (Smoker vs Non-Smoker) ")
mplt.xlabel ("Day")
mplt.ylabel ("Tip Amount")
mplt. legend (title = "Tip")
mplt.grid ()
mplt. show ()



6.	Program to plot a histogram on total_bill


•	Include title, x & y axis labels, legend for this chart
Code:
“””
program to plot a histogram on total_bill
“””

import seaborn as sb
import matplotlib.pyplot as mplt

tips = sb. load_dataset ("tips")
print ("\nFirst 5 records of iris dataset:")
print (tips.head () )

sb.histplot (data=tips, x="total_bill")
mplt. show ()
