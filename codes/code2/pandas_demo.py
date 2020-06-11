#coding=utf8
"""
Created on Wed Jan 15 23:59:56 2020

@author: Neal LONG
"""

import pandas as pd
s1=pd.Series(['a','b','c','d'])
s2=pd.Series(['a','b','c','d'],index=[101,102,103,104])
print(s1.iloc[0],s1.loc[0],s1[0],s2.iloc[0],s2.loc[101],s2[101])

df = pd.read_csv('/Users/zhangdi/ACT4311/codes/code2/wanke_price.csv')

print(df.head())

print(df.describe())

print(df.info())

print(df.index)

low2high=df[df['Open']<df['Close']][['Open','Close']]
low2high.head()

print(low2high.shape)

print(len(low2high))

print(df['Open'].mean())

print(df['Open'].std())

df['Open']+=5

print(df['Open'].mean())

def minus5(x):
    return x-5

df['Open']=df['Open'].apply(minus5)
print(df['Open'].mean())

df['l2h'] = df['Open']<df['Close']


print(df.head())

print(df.groupby('l2h')['Volume'].mean())

