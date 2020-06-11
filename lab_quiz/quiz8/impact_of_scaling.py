# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:16:24 2020

@author: Neal LONG

Suppose that you decide to removes the records with missing values 
originally exists in the "bank_marketing_train.csv", i.e., with value "unknown",
and you want to apply KNN to solve the ranking problem. While you know
KNN with Euclidean distance is sensitive to rescaling on numerical features.
In addition, you also notice that the value "999" in the feature "pdays" may 
have great impact on its value after rescaling, and may even make results worse.
Therefore, you plan to make futherdecisions by comparing the performance of KNN
 model built on following 4 different settings:
    1. KNN model built on data with attribute "pdays" (as "df_train_with_pdays" 
       below, and rescaling all numericial features by StandardScaler, use 
       OneHotEncoder to encode categorical features
    2. KNN model built on data with attribute "pdays" (as "df_train_with_pdays" 
       below, and rescaling all numericial features by Normalizer, use 
       OneHotEncoder to encode categorical features
    3. KNN model built on data without attribute "pdays" (as "df_train_without_pdays" 
       below, and rescaling all numericial features by StandardScaler, use 
       OneHotEncoder to encode categorical features
    4. KNN model built on data without attribute "pdays" (as "df_train_without_pdays" 
       below, and rescaling all numericial features by Normalizer, use 
       OneHotEncoder to encode categorical features
        
In particular, under each setting, the average AUC_ROC score during the 5-fold
 CV of KNN with best K from (100,200,300,400,500,600) is reported for comparison.

Hint:
    1. GridSearchCV could be used for choosing the best KNN and report its average
        AUC_ROC score under each settings
    2. make_column_transformer and make_column_selector could be used for performing
        the different feature engineering pipelines
    3. Answer the questions based on the comparisons
    
"""
#%%
import pandas as pd
import os
import numpy as np
from sklearn.preprocessing import  OneHotEncoder,Normalizer, StandardScaler
from sklearn.compose import make_column_transformer
from sklearn.compose import make_column_selector
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import roc_auc_score

print("\n")
print("#"*30)
print('Load training data:')
df_train_raw=pd.read_csv("./data/bank_marketing_train.csv")
print("Raw traininig data",df_train_raw.shape)
print("\n")
print("#"*30)
print('Data clean and feature engineering:')
df_train_raw = df_train_raw.astype(object).replace(to_replace={"unknown":np.nan})
df_train_raw =df_train_raw.dropna()
y_true = df_train_raw.pop('y')
df_train_with_pdays = df_train_raw
df_train_without_pdays = df_train_raw.drop('pdays',axis=1)
print("Shape of df_train_with_pdays is {} and df_train_without_pdays is {}".format(
    df_train_with_pdays.shape,df_train_without_pdays.shape))

print("\n")
print("#"*30)
print('Your code on feature engineering and validation goes below:')

setting_no=0
for d_name, df_train in zip(('data_with_pdays','data_without_pdays'),
                            (df_train_with_pdays,df_train_without_pdays)):
    ct_standard = make_column_transformer(
      (StandardScaler(),
       make_column_selector(dtype_include=np.number)),  # rating
      (OneHotEncoder(handle_unknown='ignore'),
       make_column_selector(dtype_include=object)))
        
    ct_norm = make_column_transformer(
      (Normalizer(),
       make_column_selector(dtype_include=np.number)),  # rating
      (OneHotEncoder(handle_unknown='ignore'),
       make_column_selector(dtype_include=object)))

    X_standard = ct_standard.fit_transform(df_train)
    X_norm = ct_norm.fit_transform(df_train)
    for x_name, X in zip(('with standardization','with normalization'),
                         (X_standard,X_norm)):
        print("-"*30)
        setting_no+=1
        print("Process setting {} : {} {}".format(setting_no,d_name,x_name))
        #++insert your code here (multiple lines)++ to apply  GridSearchCV 
        # for choosing the best KNN and report its average   AUC_ROC score under each settings
        knn=KNeighborsClassifier()
        best_clf = GridSearchCV(knn,scoring='roc_auc',cv=5,n_jobs=-1,
                        param_grid={'n_neighbors': [100,200,300,400,500,600]})
        best_clf.fit(X,y_true)
        print("Select best Knn model with n_neighbors = {} with best_score={}, the mean score for test_set{}.".format(
            best_clf.best_params_['n_neighbors'],
            best_clf.best_score_,
            np.mean(best_clf.cv_results_['mean_test_score'])))
# %%
