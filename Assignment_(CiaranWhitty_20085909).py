# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 16:09:19 2021

@author: Ciaran Whitty - 20085909
"""

import pandas
import numpy
import seaborn as sb
import matplotlib.pyplot as plot

from scipy import stats

#load dataset from the csv file in the dataframe called nesarc_data
covid_data = pandas.read_csv('owid-covid-data.csv',low_memory=False)

#convert all columns names to uppercase
covid_data.columns = map(str.upper, covid_data.columns)

#bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format',lambda x:'%f'%x)

#set PANDAS to show all columns in Data frame
pandas.set_option('display.max_columns', None)

print('----------------------------------------------------------------------------------------------')
print ("Starting Script") 
print('----------------------------------------------------------------------------------------------')

#rows
print ("No. of Rows in DataSet: " + str(len(covid_data))) 
#columns
print ("No. of Columns in DataSet: " + str(len(covid_data.columns))) 


#"""

print('------------------------------ Start Question 1 ------------------------------------------')

## Gets the data only for Ireland
ireSubset = covid_data[(covid_data['ISO_CODE']=='IRL')]

## Gets the data only for United Kingdom
gbrSubset = covid_data[(covid_data['ISO_CODE']=='GBR')]

print('------------------------------ Start of IRELAND ------------------------------------------')

# Start date: 29/02/2020 End date: 10/05/2021**

ire1 = ireSubset['ISO_CODE'].value_counts(sort=True)

print('counts for ISO_CODE - (No. of entries): ' + str(ire1))

print('----------------------------------------------------------------------------------------------')

print('First 20 from ireland: -')
ire2 = ireSubset[['DATE', 'ISO_CODE', 'NEW_CASES']]
ire2a = ire2.head(n=20)
print (ire2a)

### Graphs

## https://seaborn.pydata.org/examples/faceted_lineplot.html
## Relplot 2 
## Shows all ireland data on a graph starting from the beginning
sb.relplot(
    data=ire2,
    x="DATE", y="NEW_CASES",
    kind="line", size_order=["T1", "T2"],
    height=5, aspect=2, facet_kws=dict(sharex=False),
    )
plot.xlabel('Dates - 31/01/2020 10/05/2021')
plot.ylabel('New Cases')
plot.title('Graph of New Cases(Ireland)')

### Graphs

print('----------------------------------------------------------------------------------------------')

# mean, std deviation, min, max, median, mode
print('ire2 - NEW_CASES')

mean1 = ire2['NEW_CASES'].mean()
print('mean: ' + str(mean1) )

std1 = ire2['NEW_CASES'].std()
print('std deviation: ' + str(std1) )

min1 = ire2['NEW_CASES'].min()
print('min: ' + str(min1) )

max1 = ire2['NEW_CASES'].max()
print('max: ' + str(max1) )

median1 = ire2['NEW_CASES'].median()
print('median: ' + str(median1) )

mode1 = ire2['NEW_CASES'].mode()
print('mode: ' + str(mode1) )

print('------------------------------ END of IRELAND ------------------------------------------')

print('------------------------------ Start of United Kingdom ------------------------------------------')

# Start date: 31/01/2020 End date: 10/05/2021**

gbr_1 = gbrSubset['ISO_CODE'].value_counts(sort=True)

print('counts for ISO_CODE - (No. of entries): ' + str(gbr_1))

print('----------------------------------------------------------------------------------------------')

print('First 20 from United Kingdom: ')
gbr_2 = gbrSubset[['DATE', 'ISO_CODE', 'NEW_CASES']]
gbr_2a = gbr_2.head(n=20)
print (gbr_2a)

sb.set_theme(style="darkgrid")

### Graphs

## https://seaborn.pydata.org/examples/faceted_lineplot.html
## Relplot 2 
## Shows all United Kingdom data on a graph starting from the beginning
sb.relplot(
    data=gbr_2,
    x="DATE", y="NEW_CASES",
    kind="line", size_order=["T1", "T2"],
    height=5, aspect=2, facet_kws=dict(sharex=False),
    )
plot.xlabel('Dates - 31/01/2020 10/05/2021')
plot.ylabel('New Cases')
plot.title('Graph of New Cases(United Kingdom)')

### Graphs

print('----------------------------------------------------------------------------------------------')

# mean, std deviation, min, max, median, mode
print('gbr_2 - NEW_CASES')

mean1 = gbr_2['NEW_CASES'].mean()
print('mean: ' + str(mean1) )

std1 = gbr_2['NEW_CASES'].std()
print('std deviation: ' + str(std1) )

min1 = gbr_2['NEW_CASES'].min()
print('min: ' + str(min1) )

max1 = gbr_2['NEW_CASES'].max()
print('max: ' + str(max1) )

median1 = gbr_2['NEW_CASES'].median()
print('median: ' + str(median1) )

mode1 = gbr_2['NEW_CASES'].mode()
print('mode: ' + str(mode1) )


print('------------------------------ END of United Kingdom ------------------------------------------')


print('------------------------------ Start Custom Graph ------------------------------------------')

IRL_GBR = covid_data[ (covid_data['ISO_CODE']=='IRL') | (covid_data['ISO_CODE']=='GBR') ]
IRL_GBR_Subset = IRL_GBR[['DATE', 'ISO_CODE', 'NEW_CASES']]

#https://seaborn.pydata.org/tutorial/axis_grids.html

def qqplot(x, y, **kwargs):
    _, xr = stats.probplot(x, fit=False)
    _, yr = stats.probplot(y, fit=False)
    plot.scatter(xr, yr, **kwargs)

g = sb.FacetGrid(IRL_GBR_Subset, col="ISO_CODE", height=7)
g.map(qqplot, "DATE", "NEW_CASES")


print('------------------------------ End Custom Graph ------------------------------------------')

print('------------------------------ End Question 1 ------------------------------------------')

#"""

#"""
print('------------------------------ Start Question 2 ------------------------------------------')

## Data:
# Filters only countries from Europe 
# Eliminate countries with no data 
# Only countries that have population greater than 45 million
##

euroSubset = covid_data[(covid_data['CONTINENT']=='Europe') & 
                        (covid_data['REPRODUCTION_RATE'] < 10) & 
                        (covid_data['POPULATION'] > 45000000)]

#rows
print ("No. of Rows in DataSet: " + str(len(euroSubset))) 
#columns
print ("No. of Columns in DataSet: " + str(len(euroSubset.columns))) 

euro1 = euroSubset['CONTINENT'].value_counts(sort=True)

print('counts for CONTINENT - (No. of entries): ' + str(euro1))

euroSubset1 = euroSubset[['CONTINENT', 'GDP_PER_CAPITA', 'REPRODUCTION_RATE', 'ISO_CODE']]

sb.displot(data=euroSubset1, x="REPRODUCTION_RATE", hue="ISO_CODE" , kind="kde")
sb.displot(data=euroSubset1, x="REPRODUCTION_RATE", hue="ISO_CODE" , col="ISO_CODE", multiple="stack", kind="kde")

# Counts data for GDP_PER_CAPITA, ISO_CODE
a = euroSubset1['GDP_PER_CAPITA'].value_counts(sort=True, dropna=False)
b = euroSubset1['ISO_CODE'].value_counts(sort=True, dropna=False)

print (str(a)) 
print (str(b)) 

# GDP_PER_CAPITA -

# 45,229 - DEU 
# 39,753 - GBR 
# 38,605 - FRA 
# 35,220 - ITA 
# 34,272 - ESP 
# 24,765 - RUS 

print('------------------------------ End Question 2 ------------------------------------------')
#"""

#"""
print('------------------------------ Start Question 3 ------------------------------------------')

## Data: 
# 
# Data for Russia
# Data for United States
# Data for United Kingdom
# Data for Ireland
#
##

Q3 = covid_data[ (covid_data['ISO_CODE']=='RUS') | 
                (covid_data['ISO_CODE']=='USA') | 
                (covid_data['ISO_CODE']=='IRL') | 
                (covid_data['ISO_CODE']=='GBR')]

#rows
print ("No. of Rows in DataSet: " + str(len(Q3))) 
#columns
print ("No. of Columns in DataSet: " + str(len(Q3.columns))) 

Q3Subset = Q3[['DATE', 'ISO_CODE', 'NEW_VACCINATIONS', 'NEW_DEATHS']]

sb.relplot(data=Q3Subset, x="DATE", y="NEW_DEATHS", hue="ISO_CODE", kind="line", height=6, aspect=2)
plot.xlabel('Dates - 31/01/2020 10/05/2021')
plot.ylabel('New Deaths')
plot.title('Graph of New Deaths (Russia, United States, United Kingdom, Ireland)')

sb.relplot(data=Q3Subset, x="DATE", y="NEW_VACCINATIONS", hue="ISO_CODE", kind="line", height=6, aspect=2)
plot.xlabel('Dates - 31/01/2020 10/05/2021')
plot.ylabel('New Vaccinations')
plot.title('Graph of New Vaccinations (Russia, United States, United Kingdom, Ireland) ')

print('------------------------------ End Question 3 ------------------------------------------')

#"""
