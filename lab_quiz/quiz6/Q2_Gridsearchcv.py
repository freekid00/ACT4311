# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:04:11 2020

@author: Neal LONG

Use GridSearchCV (5-fold CV ,iid=False ) to select 
   the best 'C' from C_candidates, and
   the best 'gamma' from gamma_candidates 
in combination for SVC model with  random_state=0 on the training data X, and y

Note:  Use accuracy as scoring metric
"""

from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_digits

digits = load_digits()
X, y = digits.data, digits.target
gamma_candidates = [0.00001,0.00005,0.0001,0.0005,0.001,0.005,0.01,0.05,0.1]
C_candidates = [0.001,0.005,0.01,0.05,0.1,0.5,1,10,50,100,1000]


#++insert your code below++
parameters = {'gamma':gamma_candidates,
              'C':C_candidates}
svc=SVC(random_state=0)
gcv_svc = GridSearchCV(svc, parameters,cv=5,n_jobs=-1,iid=False,
                   scoring='accuracy')
gcv_svc.fit(X, y)

print("Based on GridSearchCV, the best C is {}".format(
        gcv_svc.best_params_['C']))
print("Based on GridSearchCV, the best gamma is {}".format(
        gcv_svc.best_params_['gamma']))
