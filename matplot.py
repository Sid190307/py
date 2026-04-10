1.	Program to Plot a Pine Chart
Code:
"""
write a program to plot line chart on date and open & close column
"""

import pandas as pd
import matplotlib.pyplot as mplt

#reading csv file
reliance = pd.read_csv('Reliance_Prices.csv')

#converting date column to datetime and sorting as per date
reliance['date'] = pd.to_datetime(reliance['date'], dayfirst=True)
reliance = reliance.sort_values(by = 'date')

mplt.figure(figsize = (10, 5))
mplt.plot(reliance[ "date" ], reliance[ "close" ], label= "Close")
mplt.plot(reliance[ "date" ], reliance[ "open" ], label= "Open")
mplt.title("Reliance Stock Opening & Closing Price Trends")
mplt.xlabel("Date")
mplt.ylabel("Opening / Closing Price")
mplt.grid(True)
mplt.legend()
mplt.show()


2.	Program to Plot Vertical & Horizontal Bar Chart
Code:
“””
write a program to plot bar chart on date and open & close column.
Calculate the average monthly closing price.
“””

import pandas as pd
import matplotlib.pyplot as mplt

#reading csv file
reliance = pd. read_csv ('Reliance_Prices.csv')

#converting date column to datetime and sorting as per date
reliance['date'] = pd.to_datetime (reliance['date'], dayfirst=True)
reliance = reliance.sort_values (by = 'date')

#Extracting Month
reliance["month"] = reliance["date"] .dt.month_name ()
#reliance ["month"] = reliance["date"].dt.month

#Calculate Average Close Price per month
monthly_close = reliance.groupby ("month") ["close"] .mean ()

mplt.figure(figsize = (10,5))
#mplt.bar (monthly_close. index, monthly_close. values, label="Average Close Price")

#Horizontal bars
mplt.barh (monthly_close. index, monthly_close. values, label="Average Close Price")

mplt.title ("Average Mothly Stock Opening & Closing Price Trends - Reliance")
mplt.xlabel ("Month")
mplt.ylabel ("Average Closing Price")
#mplt.grid(True) #axis='x' / 'y'

mplt. legend ()  #try legend with loc="upper right" / "upper left" / "lower right" /"lower left"
mplt.savefig ("barchart. jpg")           #To save the chart
mplt. show ()



3.	Program to Plot a Scatter Chart for Opening & Closing Price
Code:
“””
write a program to plot scatter chart on open & close column
“””

import pandas as pd
import matplotlib.pyplot as mplt

#reading csv file
reliance = pd.read_csv('Reliance_Prices.csv')

#converting date column to datetime and sorting as per date
reliance['date'] = pd.to_datetime (reliance['date'], dayfirst=True)

#Scatter Plot
mplt.figure(figsize = (10,5))
mplt.scatter (
reliance["open"],
reliance["close"],
color="red",
s=50,
alpha=0.6,
label="Average Close Price"
)

#Decoration
mplt. title ("Open vs Close Price - Reliance")
mplt.xlabel ("Open Price")
mplt.ylabel ("Close Price")
#mplt.grid(True)           #axis='x' / 'y'
mplt.legend ()  #try legend with loc="upper right" / "upper left" / "lower right" /"lower left"
#mplt.savefig ("barchart. jpg")         #To save the chart
mplt.show ()



Code:
write a program to plot scatter chart on height and weight with a line to show the correlation between points

import pandas as pd
import matplotlib.pyplot as mplt
import numpy as np

#Sample data
height = [150, 155, 160, 162, 165, 168, 170, 172, 175, 178]
weight = [45, 50, 55, 58, 60, 63, 68, 70, 75, 80]

#Line calculation
z = np.polyfit(height, weight, 1)
p= np.poly1d(z)

#Scatter Plot
mplt.figure(figsize = (10,5))
mplt.scatter(height, weight, s=60, alpha=0.5, label="Actual Data")
mplt.plot(height, p(height), color="red", label="Trend Line")

#Decoration
mplt.title("Height vs Weight")
mplt.xlabel("Height (cm)")
mplt.ylabel("Weight (kg)")
#mplt.grid(True)
mplt.legend()
#mplt.savefig("scatter. jpg")
mplt.show ()



