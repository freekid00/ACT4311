#coding=utf8
"""
Created on Thu Mar 19 00:14:26 2020

@author: Neal LONG

Construct fitting graph for decisiion tree with different max_depth 
from [1,2,3,4,5], but set the model complexity as the number of nodes 
in the tree
"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

tree_complexity = [1,2,3]
in_performance = [0.2,0.3,0.6]
out_performance = [0.1,0.6,0.3]
plt.figure(1, figsize=(6, 6))
plt.plot(tree_complexity, in_performance, label = "Train Acc.")
plt.plot(tree_complexity, out_performance, label = "Holdout Acc.")
plt.grid(True)
plt.legend()    
plt.show()


# Load data
iris = load_iris()

# Determine feature matrix X and taget array Y
X = iris.data[:,:2]
y = iris.target
clf = DecisionTreeClassifier(random_state =0)
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                    test_size=0.4, random_state= 0)


# Create and train different decision tree with different tree depth
# but random_state is always set to 0, plot the fitting graph of these 
# trees with different model complexity in terms of total number tree nodes 
# and accuracy in training data ("Train Acc.") and holdout data ("Holdout Acc.")

#++insert your code here++

tree_complexity=[]
in_performance=[]
out_performance=[]
for i in range(1,6):
    clf=DecisionTreeClassifier(random_state=0,max_depth=i)
    clf.fit(X_train,y_train)
    tree_complexity.append(clf.tree_.node_count)
    y_pred=clf.predict(X_train)
    in_per=accuracy_score(y_pred,y_train)
    in_performance.append(in_per)
    y_pred=clf.predict(X_test)
    out_per=accuracy_score(y_pred,y_test)
    out_performance.append(out_per)
    
print(tree_complexity)
print(in_performance)
print(out_performance)
plt.figure(2, figsize=(6, 6))
plt.plot(tree_complexity, in_performance, label = "Train Acc.")
plt.plot(tree_complexity, out_performance, label = "Holdout Acc.")
plt.grid(True)
plt.legend()    
plt.show()











