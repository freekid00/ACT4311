#coding=utf8
"""
Created on Wed Apr  1 23:02:25 2020

@author: Neal LONG

Use 10-Fold CV with accuracy metrics to select the best K (n_neighbors) among 
(1,3,6,9,12,15,18,21,24) for KNN with brute-force search algorithm 
when being applied on the Iris data :
    1.Plot the fitting graph 
    2.Report the best value of K

"""

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import validation_curve
import matplotlib.pyplot as plt
import numpy as np 

iris = load_iris()
X, y = iris.data, iris.target

#++insert your code below++

neighbors=[1,3,6,9,12,15,18,21,24]
knn=KNeighborsClassifier(algorithm='brute')
train_scores, test_scores = validation_curve(knn, X, y, param_name="n_neighbors", 
                                             param_range=neighbors, scoring="accuracy",
                                             n_jobs=-1, cv =10)
train_scores_mean = np.mean(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
plt.figure(1, figsize=(6, 6))
plt.plot(neighbors, train_scores_mean,marker='o',label="Mean training Acc. from 10-fold CV",
             color="darkorange")
plt.plot(neighbors, test_scores_mean,marker='o',label="Mean test Acc. from 10-fold CV",
             color="navy")
plt.grid(True)
plt.legend()
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.show()

print('The best value for neighbors is 18')

# %%
