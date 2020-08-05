'''
Created on Jan 27, 2020

@author: natra
'''
import pandas as pd
import plotly.express as px

df=pd.read_csv('C://NAT//ML & AI//testfiles/Data Sourcing/EDA_nas.csv')
df = px.data.tips()
#Box plots (boxplots)

## column count and row count
print(len(df))
print(df.columns)

fig = px.box(df, y="Maths.is.difficult")
fig.show()