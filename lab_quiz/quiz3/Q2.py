# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 22:47:16 2020

@author: Neal LONG

Modify the code to satisfy:
    1. Only use the 2-dimensional features of iris, i.e., sepal width and petal width
    2. Create the decision tree that uses "entropy" as  criterion
        refer to https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier
    3. Only plot the tree with  depth up to 4
        refer to  https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html
"""

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Load data
iris = load_iris()
iris.feature_names
## sepal width and petal width are the 1 and 3 cols
# Determine feature matrix X and taget array Y
X = iris.data[:,[1,3]]
Y = iris.target

# Create and train decision tree on all 
clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X, Y)

# Plot tree structure
plt.figure(1, figsize=(12, 12))
plot_tree(clf, filled=True,max_depth=4)
plt.show()