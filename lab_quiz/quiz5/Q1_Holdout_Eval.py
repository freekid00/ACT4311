#coding=utf8
"""
Created on Thu Mar 19 01:52:27 2020

@author: Neal LONG
Note: 
    1. Set random_state of Perceptron,LinearSVC,train_test_split to 0

"""

import pickle



with open('/Users/zhangdi/ACT4311/lab_quiz/quiz5/Q1_fetures.pkl','rb') as rf:
    X = pickle.load(rf)

with open('/Users/zhangdi/ACT4311/lab_quiz/quiz5/Q1_labels.pkl','rb') as rf:
    y = pickle.load(rf)


"""
Create three different holdout splits on X and y
 1st holdout split is choose the first 50% cases as train, and then the remaining as test
 2nd holdout split is choose the last 50% cases as train, and then the remaining as test
 3rd holdout split is choose the randomly 50% cases as train, and then the remaining as test
 Then build and evaluate the out-perfomance  of Perceptron model, 
    and LinearSVC model over different splits generated as above
Note: 
    1. Set random_state of Perceptron,LinearSVC,train_test_split to 0
    """


#++insert your code here++

from sklearn.model_selection import train_test_split
X_one_train,X_one_test,y_one_train,y_one_test=train_test_split(X,y,train_size=0.5,random_state=0,shuffle=False)
X_two_test,X_two_train,y_two_test,y_two_train=train_test_split(X,y,train_size=0.5,random_state=0,shuffle=False)
X_three_train,X_three_test,y_three_train,y_three_test=train_test_split(X,y,train_size=0.5,random_state=0,shuffle=True)

### for perceptron
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
permodel_one=Perceptron(tol=1e-3, random_state=0)
permodel_one.fit(X_one_train,y_one_train)
y_one_pred=permodel_one.predict(X_one_test)
print('Perceptron: for holdout one, the out-performance accuracy is',accuracy_score(y_one_pred, y_one_test))

permodel_two=Perceptron(tol=1e-3, random_state=0)
permodel_two.fit(X_two_train,y_two_train)
y_two_pred=permodel_two.predict(X_two_test)
print('Perceptron: for holdout two, the out-performance accuracy is',accuracy_score(y_two_pred, y_two_test))

permodel_three=Perceptron(tol=1e-3, random_state=0)
permodel_three.fit(X_three_train,y_three_train)
y_three_pred=permodel_three.predict(X_three_test)
print('Perceptron: for holdout three, the out-performance accuracy is',accuracy_score(y_three_pred, y_three_test))


### for LinearSVC
from sklearn.svm import LinearSVC
s_one=LinearSVC(tol=1e-3, random_state=0)
s_one.fit(X_one_train,y_one_train)
y_one_pred=s_one.predict(X_one_test)
print('LinearSVC: for holdout one, the out-performance accuracy is',accuracy_score(y_one_pred, y_one_test))

s_two=LinearSVC(tol=1e-3, random_state=0)
s_two.fit(X_two_train,y_two_train)
y_two_pred=s_two.predict(X_two_test)
print('LinearSVC: for holdout two, the out-performance accuracy is',accuracy_score(y_two_pred, y_two_test))

s_three=LinearSVC(tol=1e-3, random_state=0)
s_three.fit(X_three_train,y_three_train)
y_three_pred=s_three.predict(X_three_test)
print('LinearSVC: for holdout three, the out-performance accuracy is',accuracy_score(y_three_pred, y_three_test))





