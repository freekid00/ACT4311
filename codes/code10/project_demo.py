#coding=utf8
"""
Created on Mon Apr 13 15:03:51 2020

@author: Neal LONG

Using xgboost for the individual project


conda install xgboost  (for Linux or Mac OS)
or
conda install py-xgboost (for Windows)
"""
#%%
import pandas as pd
import os
import numpy as np
# from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import  OneHotEncoder,LabelEncoder
from sklearn.compose import make_column_transformer
from sklearn.compose import make_column_selector
import xgboost as xgb

print("\n")
print("#"*30)
print('Load training data:')
df_train=pd.read_csv("./data/bank_marketing_train.csv")
# for comparison on smaller data
# df_train = pd.read_pickle(os.path.join(data_dir,"bank-compain-example.pickle"))
# df_train['age'] =  pd.to_numeric(df_train['age'])

print(df_train.shape)

print("\n")
print("#"*30)
print('Data clean and feature engineering:')

df_train = df_train.astype(object).replace(to_replace={"unknown":np.nan})
cat_columns = df_train.select_dtypes(include='object').columns
cat_columns = cat_columns.drop('y')
df_train =df_train.dropna(subset=cat_columns, inplace=False)

# df_train =df_train.dropna( subset=cat_columns, inplace=False)
print(df_train.shape)
#%%
y = df_train.pop('y')

columns_in_train = df_train.columns
ct = make_column_transformer((OneHotEncoder(handle_unknown='ignore'),
       make_column_selector(dtype_include=object)),remainder='passthrough')
X = ct.fit_transform(df_train)
label_encoder = LabelEncoder()

y = label_encoder.fit_transform(y)
print(X.shape,len(X),len(y))

# Model selection
print("\n")
print("#"*30)
print('Model selection:')
clf = xgb.XGBRFClassifier()

clf.fit(X,y)



# Model application 
print("\n")
print("#"*30)
print('Model Application with missing values:')
df_test=pd.read_csv("./data/bank_marketing_test.csv")
df_test = df_test.astype(object).replace(to_replace={"unknown":np.nan})
scores = pd.Series(index=df_test.index,dtype=np.float64)
vld_index = df_test.index[df_test[cat_columns].notnull().all(axis=1)] 
df_test_val =df_test.dropna(subset=cat_columns, inplace=False)
assert len(vld_index) == len(df_test_val)

df_test_val = df_test_val[columns_in_train]
X_new_val = ct.transform(df_test_val)
probas_vals = clf.predict_proba(X_new_val)
print(clf.classes_,label_encoder.transform(['yes']))
pos_label = label_encoder.transform(['yes'])[0]

#first and the only index for positive label
pos_index = np.where(clf.classes_ ==pos_label)[0][0]

#construct the prediction with associated index
scores_vals_series = pd.Series([proba[pos_index] for proba in probas_vals],index=vld_index)
#fill the valid prediction scores
scores.update(scores_vals_series)

#fill the scores  for rows with missing value to the minimum score
scores = scores.fillna(0.49)

assert all(pd.notnull(scores))
assert len(scores)==len(df_test)
print('Predict {} valid scores for {} examples in final test'.format(len(probas_vals),len(df_test)))


# %%
