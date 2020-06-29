# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:57:07 2020

@author: moham
"""
#data path to use in Notebook: C:\Users\moham\AppData\Local\Temp\spyder\notebooks
import pandas as pd
df = pd.read_csv('ETH_1h.csv')
df.head()
df.shape
df['Date']
df.loc[0, 'Date'].day_name() #error. we need to change its type to datetime
df['Date'] = pd.to_datetime(df['Date']) #another error because of the formatting in the file.
df['Date'] = pd.to_datetime(df['Date'], format = '%Y-%m-%d %I-%p') #using the python formatting document, we tell pandas how to parse our date in the file using python formatting guide.
df['Date'] #check to see if converting worked well.
df.loc[0, 'Date'].day_name() #now it works! #it can be done at the beginning when loading the file. As follow:
#changing format when reading the file:
d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %I-%p')    
df = pd.read_csv('ETH_1h.csv', parse_dates=['Date'], date_parser=d_parser  )  
df.loc[0,'Date']
df['Date'].dt.day_name() #show day name for all the rows in 'Date' column.
##so using a dt class on a series object is similar to how we access the string class or the str class for the string methods on an entire series.
df['DayOfWeek']=df['Date'].dt.day_name() #creates a new column with day names in it.
df['DayOfWeek']
df['Date'].min() #earliest date in file.
df["Date"].max() #latest date in file.
df["Date"].max() - df['Date'].min() #duration between the earliest and latest date in file.
filt = (df['Date']>='2020') #creates a filter for dates from and after 2020
df.loc[filt] #shows the outcome of filter
filt = (df['Date'] >= '2019') & (df['Date'] < '2020') #creates a filter for dates between 2019 and 2020.#
#We're using strings here: '2019' and '2020'. We can also use actual datetimes as follow:
filt = (df['Date'] >= pd.to_datetime('2019-01-01')) & (df['Date'] < pd.to_datetime('2020-01-01')) #same as above, just using datetimes instead of strings.
#if we set our index to be the dates, then we can do the same thing by using slicing instead. first let's set the index:
df.set_index('Date', inplace=True) #"date' becomes the index for the dataframe.
df['2019'] #shows data for 2019
df['2020-01': '2020-02'] #grab dates for a specific range using SLICING.
df['2020-01': '2020-02']['Close'] #shows the 'Close' value for this range.
df['2020-01': '2020-02']['Close'].mean() #shows the average of 'Close' column for the range.
df['2020-01-01']['High'] #shows values under 'High' column for that day.
df['2020-01-01']['High'].max() #shows max value under 'High' for that day.
#currently this data is broken down on an hourly basis, if we want to redo this ao that it is broken down by day or week, or month we can do this by RESAMPLING:
#should look it up in pandas documnetation for different time indicators, for example D for daily, W for weekly.
df['High'].resample('D').max()#gives a series with high values for each day.
highs = df['High'].resample('D').max()#create a variable with the above assignment. 
highs['2020-01-01'] #gives 
highs.plot() #plots highs
df.resample('W').mean() #gives the mean values for each of these columns on a weekly basis.
#to resample and use multiple columns, also use multiple aggregation methods. AGG method is used for this:
#Here is how to resample multiple columns (closing column, high and low columns, and also the volume)
#and grabbing different values for each, for example mean for close column, max for High column, etc.
df.resample('W').agg({'Close':'mean', 'High': 'max', 'Low': 'min', 'Volume': 'sum'})
