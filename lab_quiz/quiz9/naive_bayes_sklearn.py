# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 23:17:07 2020
@author: Neal LONG

This question aims to encourage you learn more about different implementation
 of Naive Bayes model in Sklearn by comparing the performance of CategoricalNB,GaussianNB under following two settings:

setting-1. Use KBinsDiscretizer to discretize attribute 'Temperature' into 3 ordinal
     levels, and discretize attribute 'Humidity' into 2 ordinal levels and use
     OrdinalEncoder to encode two remaining features 'Outlook','Wind',
     as X in the following;

setting-2. Use KBinsDiscretizer to discretize attribute 'Temperature' into 3 ordinal
     levels, and discretize attribute 'Humidity' into 2 ordinal levels and use
     OneHotEncoder to encode two remaining features 'Outlook','Wind';
     
     
Evaluate and compare the average accuracy score of CategoricalNB,GaussianNB 
from a 5-fold cross validation underabove two settings.


Hint:
1. Please refer to https://scikit-learn.org/stable/modules/classes.html#module-sklearn.naive_bayes to learn more about Naive Bayes, especially CategoricalNB,GaussianNB;

"""
#%%
import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer,OrdinalEncoder, OneHotEncoder
from sklearn.compose import make_column_transformer

df = pd.read_csv('./golf.csv')
print(df.info())
y= df.pop('Play').values
ct_1 = make_column_transformer(
      (KBinsDiscretizer(3,encode='ordinal'),
       ['Temperature']),  
      (KBinsDiscretizer(2,encode='ordinal'),
       ['Humidity']),
      (OrdinalEncoder(),
      ['Outlook','Wind']))
ct_2 = make_column_transformer(
      (KBinsDiscretizer(3,encode='ordinal'),
       ['Temperature']),  
      (KBinsDiscretizer(2,encode='ordinal'),
       ['Humidity']),
      (OneHotEncoder(),
      ['Outlook','Wind']))
one_X = ct_1.fit_transform(df)
two_X= ct_2.fit_transform(df)
#%%
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB, CategoricalNB
import numpy as np 
ngb=GaussianNB()
sc_1=cross_val_score(ngb,X=one_X,y=y,scoring='accuracy',cv=5)
print('the avg score for GassianNB in setting one is',np.mean(sc_1))
# %%
cgb=CategoricalNB()
sc_2=cross_val_score(cgb,X=one_X,y=y,scoring='accuracy',cv=5)
print('the avg score for CategoryNB in setting one is',np.mean(sc_2))
# %%
ngb=GaussianNB()
sc_1=cross_val_score(ngb,X=two_X,y=y,scoring='accuracy',cv=5)
print('the avg score for GassianNB in setting two is',np.mean(sc_1))
# %%
cgb=CategoricalNB()
sc_2=cross_val_score(cgb,X=two_X,y=y,scoring='accuracy',cv=5)
print('the avg score for CategoryNB in setting two is',np.mean(sc_2))

# %%
