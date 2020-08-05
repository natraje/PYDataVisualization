'''
Created on Dec 26, 2019

@author: natra
'''

import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt
import seaborn as sns

#Set style grd
sns.set_style('whitegrid')
df=pd.read_csv('C://NAT//ML & AI//testfiles/market_fact.csv')
df.loc[pd.isnull(df['Shipping_Cost']),['Shipping_Cost']]=0
## Histogram
sns.distplot(df['Shipping_Cost']) #it is histogram
plt.title('Histogram')
plt.show()
## RugPlot
sns.distplot(df['Shipping_Cost'][:200],rug=True) 
plt.title('Rug Plot with first 200')
plt.show()


sns.distplot(df['Sales'][:1000], rug=True) 
plt.title('Rug Plot with first 1000')
plt.show()
##Box plot
sns.boxplot(df['Order_Quantity'])
plt.title('Box Plot')
plt.show()

## Bivariate distribution
sns.jointplot('Sales','Profit',df)
plt.title('BiVariate')
plt.show()

df=df[((df['Profit']>0) & (df['Profit']<10000)) & (df['Sales']<20000)]
sns.jointplot('Sales','Profit',df)
plt.title('BiVariate inspect dense area')
plt.show()