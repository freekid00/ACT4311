# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 21:52:09 2020

@author: Neal LONG
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load data
iris = load_iris()

# We only take the first two corresponding features
X = iris.data[:, :2]
Y_true = iris.target

# Create an instance of DecisionTreeClassifier with all default parameters
tree = DecisionTreeClassifier()

#and fit the data with true label
tree.fit(X, Y_true)

#Compute the predicted label
Y_pred =  tree.predict(X)
err_idx = []
for i in range(len(Y_pred)):
    if Y_pred[i] !=Y_true[i]: 
    # if the predicted label of i-th case does not match its true label
        print(Y_pred[i],Y_true[i])
        err_idx.append(i)

X_error = X[err_idx]


# Plot the decision boundary. For that, we will assign a color to each
# point in the mesh [x_min, x_max]x[y_min, y_max].
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
h = .01  # step size in the mesh
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = tree.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(1, figsize=(8, 8))
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.RdYlBu)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

# Plot also the training points
plt.scatter(X[:, 0], X[:, 1], c=Y_true, edgecolors='k', s=100, cmap=plt.cm.RdYlBu)
plt.title("Decision surface of a decision tree ")
plt.axis("tight")
# Also plot error points
plt.scatter(X_error[:, 0], X_error[:, 1], c='r', marker='x')





plt.show()