# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:36:39 2020

@author: Neal LONG
"""
#%%
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.compose import make_column_selector
from sklearn.metrics import roc_auc_score

data_dir = r'./data'
# Load the data
df_raw=pd.read_pickle(os.path.join(data_dir,"bank_marketing_for_clean_example.pickle"))
# df_raw=pd.read_csv(os.path.join(data_dir,"bank_marketing_train.csv"))
#%%
# Understand basic information about data
print("\n")
print("#"*30)
print('Basic info. of raw data:')
print(df_raw.shape)
print(df_raw.info(verbose=True))
#print(df_raw.head(5))
#%%
# Based on description, repalce the all the missing value defined as 
# "unknown" by missing value in Numpy, i.e., numpy.nan 
df = df_raw.astype(object).replace(to_replace={"unknown":np.nan})

# check missing data
print("\n")
print("#"*30)
print('Missing data summary for columns as follows:')
print(df.isnull().sum().sort_values(ascending=False))
#%%
# Perform some exploratory data analysis (EDA)
print('EDA on the raw data as follows:')

plt.figure()
df['campaign'].plot.hist(bins=20, title="campaign")
plt.show()

plt.figure()
df['pdays'].plot.hist(bins=20, title="pdays")
plt.show()
#%%

# Fix data type error and range errors in column-age
print("\n")
print("#"*30)
print('Before fix data type:',df['age'].dtype)
df['age'] =  pd.to_numeric(df['age'])
print('After fix data type:',df['age'].dtype)
print('Before fix out-of-range errors')
#%%
plt.figure()
df['age'].plot.hist(bins=20, title="age(before fix range)")
plt.show()

df.loc[(df['age']<0)|(df['age']>100),'age'] =  np.nan
plt.figure()
df['age'].plot.hist(bins=20, title="age(after fix range)")
plt.show()
#%%
# Fix obivous typos 
print("\n")
print("#"*30)
print('Fix obivous typos in column-marital')
print('Before fix typos:',df['marital'].unique())
df['marital'] = df['marital'].replace(to_replace={"sungle":"single"})
print('After fix typos:',df['marital'].unique())
#%%
# Fix consistency errors
print("\n")
print("#"*30)
print("""Process in-consistency among columns ('pdays','previous', 'poutcome')""")
print("All values for poutcome for examples with previous=0 are'nonexistent'?",
      all(df.loc[df['previous'] ==0,'poutcome']=='nonexistent'))
print("All values for previous for examples with poutcome='nonexistent' are 0?",
      all(df.loc[df['poutcome'] == 'nonexistent','previous']==0))

print("All pdays for examples with poutcome='nonexistent' are 999?",all(df.loc[df['poutcome'] == 'nonexistent','pdays']==0))
print("Before fix,All poutcome for examples with pdays=999 are 'nonexistent'?",all(df.loc[df['pdays'] ==999,'poutcome']=='nonexistent'))
df.loc[(df['pdays'] ==999) & (df['poutcome'] !='nonexistent'),'pdays'] = np.nan
print("After fix, All poutcome for examples with pdays=999 are 'nonexistent'?",all(df.loc[df['pdays'] ==999,'poutcome']=='nonexistent'))
#%%
# Fix outliers
print("\n")
print("#"*30)
print('Process outliers in column-campaign')
q1,q3 = df['campaign'].quantile([0.25,0.75])
lower = q1 - 3*(q3-q1)
upper = q3 + 3*(q3-q1)

df.loc[(df['campaign']<lower)|(df['campaign']>upper),'campaign'] = np.nan
plt.figure()
df['campaign'].plot.hist(bins=20, title="campaign (fixed outliers)")
plt.show()
#%%


# Check missing data
print("\n")
print("#"*30)
print('Missing data summary for columns as follows:')
print(df.isnull().sum().sort_values(ascending=False))
#%%
# Fill missing value in column-job with domain knowledge
print("\n")
print("#"*30)
print('Fix missing value in column-job with domain knowledge:')
print(df.loc[(df['age'] >60) & pd.isnull(df['job'] ),'job'] )
df.loc[(df['age'] >60) & pd.isnull(df['job'] ),'job'] = 'retired'
print("All the job information for examples older than 60 are valid?",all(pd.notnull(df.loc[df['age'] >60,'job'])))
#%%
# Fill missing value in column-loan with majority
print("\n")
print("#"*30)
print('Fix missing value in column-loan with majority:')
imp = SimpleImputer(strategy='most_frequent')
df[['loan']] = imp.fit_transform(df[['loan']])
print("All the loan  for examples are valid?",all(pd.notnull(df['loan'])))
#%%

# Fill missing value in column-loan with linear interpolation
print("\n")
print("#"*30)
print('Fix missing value in column-campaign with linear interplotion:')
df.set_index('previous',inplace=True)
df['campaign'] = df['campaign'].interpolate('linear')
df.reset_index(inplace=True)
print("All the campaign for examples are valid?",all(pd.notnull(df['campaign'])))
#%%
# Drop Missing records
print("\n")
print("#"*30)
print('Drop records with any missing values:')
print("Before drop, the shape of data is",df.shape)
df = df.dropna()
print("After drop, the shape of data is",df.shape)


# Deal with class imbalance by over-sampling the positive cases
print("\n")
print("#"*30)
print('Fix imbalanced data:')
class_priors_pos = (df['y']  == 'yes').sum()
class_priors_neg = (df['y']  == 'no').sum()
print("There are {} positive examples and {} negative examples in the data set".format(
        class_priors_pos,class_priors_neg))

df_pos = df[df['y'] == 'yes']
df_neg = df[df['y']  == 'no']
df_pos_over = df_pos.sample(int(0.5*class_priors_neg), replace=True)
df = pd.concat([df_pos_over,df_neg])
class_priors_pos = (df['y']  == 'yes').sum()
class_priors_neg = (df['y']  == 'no').sum()
print("After over-sampling, there are {} positive examples and {} negative examples in the data set".format(
        class_priors_pos,class_priors_neg))
#%%
# Feature engineering
print("\n")
print("#"*30)
print('Feature engineering:')
# Add one non-linear feature to represent how many contacts on average in this campain
# df['contacts_daily'] = df['campaign']/(df['pdays']+1)
df = df.assign(contacts_daily=(df['campaign']/(df['pdays']+1)).values)
# Extract lables
y = df.pop('y').values
columns_in_train = df.columns
#%%
# Perform standardlization on numerical features and use OneHotEncoder to encode
# categorical features
ct = make_column_transformer(
      (StandardScaler(),
       make_column_selector(dtype_include=np.number)),  #numerical features
      (OneHotEncoder(handle_unknown='ignore'),
       make_column_selector(dtype_include=object))) # categorical features
X = ct.fit_transform(df)
print(X.shape,len(X),len(y))
#%%
# Model selection
print("\n")
print("#"*30)
print('Model selection:')
clf = SVC()
# Select best C for SVC by AUC score of ROC curve
best_clf = GridSearchCV(clf,scoring='roc_auc',cv=5,n_jobs=-1,
                        param_grid={'C': [0.01, 0.1, 1, 10, 100,500,1000]})
best_clf.fit(X,y)
print("Select best SVC model with C = {} with best_score={}".format(
    best_clf.best_params_['C'],
    best_clf.best_score_))
y_true=y
y_true[y_true=='yes']=1
y_true[y_true=='no']=0
print("The avarage AUC_ROC of the best SVC from 5-fold CV on training data is",
      roc_auc_score(y_true.tolist(),best_clf.decision_function(X).tolist()))
#%%
# Model application 
print("\n")
print("#"*30)
print('Model Application with potential mistakes:')
df_test=pd.read_csv("./data/bank_marketing_test.csv")
df_test = df_test.astype(object).replace(to_replace={"unknown":np.nan})
scores = pd.Series(index=df_test.index,dtype=np.float64)
vld_index = df_test.index[df_test.notnull().all(axis=1)] 
df_test_val = df_test.dropna()
assert len(vld_index) == len(df_test_val)


df_test_val = df_test_val.assign(contacts_daily=(df_test_val['campaign']/(df_test_val['pdays']+1)).values)
df_test_val = df_test_val[columns_in_train]
X_new_val = ct.transform(df_test_val)
scores_vals = best_clf.decision_function(X_new_val)

#construct the prediction with associated index
scores_vals_series = pd.Series(scores_vals,index=vld_index)
#fill the valid prediction scores
scores.update(scores_vals_series)
#fill the scores  for rows with missing value to the minimum score
scores = scores.fillna(min(scores_vals))
# scores = scores.fillna(-min(abs(scores_vals)))

assert all(pd.notnull(scores))
assert len(scores)==len(df_test)
print('Predict {} scores for {} examples in final test'.format(len(scores_vals),len(df_test)))
#%%