# -*- coding: utf-8 -*-
"""Stock Market 1.0.ipynb


# Stock Market Analysis During Covid-19 start

### In this article we have picked 4 stocks and tried to analyze its prices during Covid-19 outbreak.

## Lets start by importing all the required libraries and datasets
"""

import pandas as pd
import datetime

"""## Datasets can be downloaded from [here.](https://github.com/Ketaki72/Stock-Market-Analysis-During-Covid19/tree/main/Datasets)

## Use Pandas library to read csv and store it in Dataframe ,Also set date column as our Index.
"""

infy = pd.read_csv('/content/INFY.NS.csv',header=0,index_col='Date',parse_dates=True)   
tcs = pd.read_csv('/content/TCS.NS.csv',header=0,index_col='Date',parse_dates=True)
wipro = pd.read_csv('/content/WIPRO.NS.csv',header=0,index_col='Date',parse_dates=True)
techm = pd.read_csv('/content/TECHM.NS.csv',header=0,index_col='Date',parse_dates=True)

"""Lets see how is our data and the columns it contains."""

infy.head(3)    #see first 3 rows

infy.tail(3)   #see last 3 rows

"""## Know your data!

## Pandas describe() is used to view some basic statistical details like percentile, mean, std etc.
"""

infy.describe()

infy.columns  # to see available columns

infy.index #check index to verify the data type

infy.shape #to get shape of our datframe

"""## Now that we have loaded our dataset and data is already cleaned and ready for us to Visualize.

### Lets begin by importing matplolib for data visualization...
"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt   #for visualization
import matplotlib.dates as mdates #for date plotting
import seaborn as sns
sns.set_theme(context='notebook',style='darkgrid')

# %matplotlib inline

"""Let's plot on Adj Close prices"""

plt.figure(figsize=(12,7))
plt.plot(infy.index ,infy['Adj Close'],color='b') #Plot on Adj close
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Chose the format for date 
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.xticks(rotation=70)
plt.title('Infosys Stock Price from Sept 2019 - Nov 2021',fontdict={'fontsize':20,'color':'Blue'},pad=10)
plt.xlabel('Date range Sept 2019 - Nov 2021')
plt.ylabel('Stock Prices')
plt.show()

"""From above graph it is clear there was a fall in March 2020 let's see closely ..
Here we have selected time range 2020-03-01 to 2020-05-01 when Covid-19 outbreak started.

# Zooming in Data

Below graph shows its effect on Stock prices, as We can see there is a drastic fall in price starting March.
"""

#Subplots

f,ax = plt.subplots(2,2,figsize =(10,10),sharex = True)
f.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
f.gca().xaxis.set_major_locator(mdates.MonthLocator())

#infy
infy1920 = infy.loc[pd.Timestamp('2020-03-01'):pd.Timestamp('2020-05-01')]
ax[0,0].plot(infy1920.index,infy1920['Adj Close'],'-o',color='r')
ax[0,0].grid(True)
ax[0,0].tick_params(labelrotation=60)
ax[0,0].set_title('INFOSYS');


tcs1920 = tcs.loc[pd.Timestamp('2020-03-01'):pd.Timestamp('2020-05-01')]
ax[0,1].plot(tcs1920.index,tcs1920['Adj Close'],'-o',color='g')
ax[0,1].grid(True)
ax[0,1].tick_params(labelrotation=60)
ax[0,1].set_title('TCS');


wipro1920 = wipro.loc[pd.Timestamp('2020-03-01'):pd.Timestamp('2020-05-01')]
ax[1,1].plot(wipro1920.index,wipro1920['Adj Close'],'-o',color='b')
ax[1,1].grid(True)
ax[1,1].tick_params(labelrotation=60)
ax[1,1].set_title('WIPRO');


techm1920 = techm.loc[pd.Timestamp('2020-03-01'):pd.Timestamp('2020-05-01')]
ax[1,0].plot(techm1920.index,techm1920['Adj Close'],'-o',color='y')
ax[1,0].grid(True)
ax[1,0].tick_params(labelrotation=60)
ax[1,0].set_title('TECH MAHINDRA');
plt.suptitle('Stock Analysis During Covid Breakdown in India',fontsize=20);

# set labels
plt.setp(ax[1,0], xlabel='Data Range from March to May 2020');
plt.setp(ax[1,0], ylabel='Stock Prices');

"""This is how you can zoom in your data and analyze for a particular range of dates.

From above graph we can see there was a significant dip in prices during mid March.

Hope this helps you get started !

Happy Learning :-)




"""

