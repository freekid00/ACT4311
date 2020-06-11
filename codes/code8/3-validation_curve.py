# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:00:09 2020

@author: Neal LONG


Advantages of using validation_curve:
    0. Less code
    1. Concurrent execution with n_jobs >1
    2. Detailed  train and test scores for every fold and every model

"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score,train_test_split,validation_curve
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

# Load data
iris = load_iris()

# Determine feature matrix X and taget array Y
X = iris.data[:,:2]
y = iris.target
candidate_max_depth = [1,2,3,4,5,6]


##########
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                test_size=0.4, random_state= 0)
in_performance = []
out_performance = []
max_depths = [1,2,3,4,5,6]
for d in max_depths:
    clf = DecisionTreeClassifier(max_depth=d,random_state=0)
    clf.fit(X_train, y_train)  
    y_train_pred = clf.predict(X_train)
    y_test_pred = clf.predict(X_test)
    in_performance.append(accuracy_score(y_train_pred, y_train))
    out_performance.append(accuracy_score(y_test_pred, y_test))
    
plt.figure(1, figsize=(8, 8))
plt.plot(candidate_max_depth, in_performance,marker='o',label="Training Acc.",
             color="darkorange")
plt.plot(candidate_max_depth, out_performance,marker='o',label = "Holdout Acc.",
             color="navy")
plt.ylabel("Accuracy")
plt.xlabel("max_depth")
plt.title('Choose best max_depth with singel holdout split') 

plt.grid(True)
plt.legend()    
plt.show()



##########
out_performance = []
in_performance = []

for d in candidate_max_depth:
    clf = DecisionTreeClassifier(max_depth=d, random_state=0)
    cv_scores = cross_val_score(clf, X, y, cv=5,
                                scoring='accuracy')
    out_performance.append(np.mean(cv_scores))
plt.figure(1, figsize=(8, 8))
plt.ylabel("Accuracy")
plt.xlabel("max_depth")
plt.plot(candidate_max_depth, out_performance,color="navy",marker='o',
         label = "Mean test Acc. from 5-fold CV")
plt.grid(True)
plt.legend()    
plt.title('5-fold CV Curve for Decision Tree on max_depth by cross_val_score') 
plt.show()


##########


base_clf = DecisionTreeClassifier(random_state=0)
train_scores, test_scores = validation_curve( base_clf, X, y, param_name="max_depth", 
    param_range=candidate_max_depth, scoring="accuracy", n_jobs=-1, cv =5)
train_scores_mean = np.mean(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
plt.figure(1, figsize=(8, 8))
plt.ylabel("Accuracy")
plt.xlabel("max_depth")
plt.title("K-fold(k={}) CV Curve for Decision Tree on max_depth by validation_curve".format(train_scores.shape[1]))

plt.plot(candidate_max_depth, train_scores_mean,marker='o',label="Mean training Acc. from 5-fold CV",
             color="darkorange")
plt.plot(candidate_max_depth, test_scores_mean,marker='o',label="Mean test Acc. from 5-fold CV",
             color="navy")
plt.grid(True)
plt.legend()
plt.show()

