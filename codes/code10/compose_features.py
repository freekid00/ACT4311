#coding=utf8
"""
Created on Mon Apr 12 12:20:26 2020

@author: Neal LONG
"""
#%%
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.compose import make_column_selector
import pandas as pd  
import numpy as np
X = pd.DataFrame({'city': ['London', 'London', 'Paris', 'Sallisaw'],
                  'rating': [5, 3, 4, 5]})  
print(X.head())
#%%
ct = make_column_transformer(
      (StandardScaler(),
       make_column_selector(dtype_include=np.number)),  # rating
      (OneHotEncoder(handle_unknown='ignore'),
       make_column_selector(dtype_include=object)))  # city

print("\nAfter transformation")
ct.fit_transform(X)
#%%

X_new = pd.DataFrame({'city': ['Beijing', 'Paris'],
                  'rating': [5, 3]})  
print("\nApply to new data")
print(ct.transform(X_new))

# %%
