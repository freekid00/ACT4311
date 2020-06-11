#%%
import pandas as pd 
import numpy as np 
train=pd.read_csv('cs-training.csv',index_col=False)

# %%
print(train.shape)
train.head()

# %%
print(train.SeriousDlqin2yrs.value_counts())
train_x=train.drop('SeriousDlqin2yrs',axis=1)
train_y=train['SeriousDlqin2yrs']

# %%
from sklearn.impute import SimpleImputer
from sklearn.ensemble import ExtraTreesRegressor
# imp=SimpleImputer(strategy='mean')
# x_ceshi=imp.fit_transform(train_x)
# model=ExtraTreesRegressor(n_jobs=-1,n_estimators=200,max_depth=20,max_features=0.5,random_state=0)
# model.fit(x_ceshi,train_y)

# # %%
# features=train_x.columns.values
# importances=model.feature_importances_
# importance_std=np.std([tree.feature_importances_ for tree in model.estimators_],axis=0)
# fea_df=pd.DataFrame({'features':features,'importances':importances,'imp_std':importance_std})
# # %%
# fea_df.sort_values('importances',ascending=False)

# %%
## fix RevolvingUtilizationOfUnsecuredLines
q1,q3=train_x['RevolvingUtilizationOfUnsecuredLines'].quantile([0.25,0.75])
lower = q1 - 3*(q3-q1)
upper = q3 + 3*(q3-q1)
train_x.loc[(train_x['RevolvingUtilizationOfUnsecuredLines']>=upper)|(train_x['RevolvingUtilizationOfUnsecuredLines']<=lower),'RevolvingUtilizationOfUnsecuredLines']=np.nan 
train_x.loc[(train_x['RevolvingUtilizationOfUnsecuredLines']>=1),'RevolvingUtilizationOfUnsecuredLines']=np.nan 
# %%
### fix age
train_x.loc[(train_x['age']==0),'age']=np.nan 

# %%
## fix NumberOfTime30-59DaysPastDueNotWorse
train_x.loc[(train_x['NumberOfTime30-59DaysPastDueNotWorse']>90),'NumberOfTime30-59DaysPastDueNotWorse']=np.nan 

# %%
## fix DebtRatio
q1,q3=train_x['DebtRatio'].quantile([0.25,0.75])
lower = q1 - 3*(q3-q1)
upper = q3 + 3*(q3-q1)
train_x.loc[(train_x['DebtRatio']>=upper)|(train_x['DebtRatio']<=lower),'DebtRatio']=np.nan 

# %%
## fix MonthlyIncome
q1,q3=train_x['MonthlyIncome'].quantile([0.25,0.75])
lower = q1 - 3*(q3-q1)
upper = q3 + 3*(q3-q1)
train_x.loc[(train_x['MonthlyIncome']>=upper)|(train_x['MonthlyIncome']<=lower),'MonthlyIncome']=np.nan 

# %%
## fix NumberOfTimes90DaysLate and NumberOfTime60-89DaysPastDueNotWorse
train_x.loc[(train_x['NumberOfTimes90DaysLate']>90),'NumberOfTimes90DaysLate']=np.nan 
train_x.loc[(train_x['NumberOfTime60-89DaysPastDueNotWorse']>90),'NumberOfTime60-89DaysPastDueNotWorse']=np.nan 

# %%
# from sklearn.impute import SimpleImputer
# knn_col=['DebtRatio','MonthlyIncome']
# knn_df=train_x[knn_col]
# without_knn_df=train_x.drop(knn_col,axis=1)
# without_knn_df_cols=without_knn_df.columns.values
# imp=SimpleImputer(strategy='mean')
# without_knn_df=imp.fit_transform(without_knn_df)
# without_knn_df=pd.DataFrame(without_knn_df,columns=without_knn_df_cols)

# %%
# train_x=pd.concat([knn_df,without_knn_df],axis=1)
# train_x.head()

# %%
# from sklearn.impute import KNNImputer
# knn_=KNNImputer(n_neighbors=5)
# train_x=knn_.fit_transform(train_x)

# %%
from sklearn.impute import SimpleImputer
col_names=list(train_x.columns)
imp=SimpleImputer(strategy='mean')
train_x=imp.fit_transform(train_x)
train_x=pd.DataFrame(train_x,columns=col_names)
total=train_x
total['SeriousDlqin2yrs']=train_y
total.to_csv('./train_x.csv')
#%%
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
lg=LogisticRegression(C=1)
best_clf=GridSearchCV(lg,param_grid={'C':[0.001,0.01,0.1,1]},n_jobs=-1,scoring='roc_auc')
best_clf.fit(train_x,train_y)
print(best_clf.best_params_,best_clf.best_score_)
# %%
from sklearn.ensemble import RandomForestClassifier
rd=RandomForestClassifier(random_state=42,n_jobs=-1)
rd_clf=GridSearchCV(rd,param_grid={'n_estimators':[50,100,200,300]},n_jobs=-1,scoring='roc_auc')
rd_clf.fit(train_x,train_y)
print(rd_clf.best_params_,rd_clf.best_score_)

# %%
from lightgbm.sklearn import LGBMClassifier
clf = LGBMClassifier(random_state = 50, n_jobs = -1)
best_clf = GridSearchCV(clf,scoring='roc_auc',cv=5,n_jobs=-1,
                        param_grid={'n_estimators': [50,100,200],
                        'reg_lambda':[0.5,1,1.5]})
best_clf.fit(train_x,train_y)
print("Select best LGB model with n_estimators = {} and reg_lambda={} with best_score={}".format(
    best_clf.best_params_['n_estimators'],best_clf.best_params_['reg_lambda'],
    best_clf.best_score_))

# %%
