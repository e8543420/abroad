# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 12:28:51 2017

@author: zhaox
"""

import pandas as pd
import numpy as np

df=pd.read_csv('C:/python/abroad/trends/data2.csv')
new_name=list(df.columns)
new_name[0]='date'
df.columns=new_name
df.date=pd.to_datetime(df.date)
year=pd.Series([x.year for x in df.date])
df['year']=year
year_mean=df.groupby('year').mean()