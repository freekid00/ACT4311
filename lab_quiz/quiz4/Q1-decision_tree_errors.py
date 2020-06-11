# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 22:30:42 2020

@author: Neal LONG

count the zero-one loss of decision tree with different max_depth 
from [1,2,3,4,5], but random_state is always set to 0 
"""


from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load data
iris = load_iris()

# Determine feature matrix X and taget array Y
X = iris.data
Y_true = iris.target
clf = DecisionTreeClassifier(random_state =0)
clf.fit(X, Y_true)
Y_Pred = clf.predict(X)
print("This trained decision tree has {} nodes".format(clf.tree_.node_count))


# Create and train different decision tree with different tree depth
# then count error and corresponding total number of nodes

#++insert your code here++
only_loss={}
for depth in range(1,6):
    clf=DecisionTreeClassifier(random_state =0,max_depth=depth)
    clf.fit(X, Y_true)
    Y_Pred = clf.predict(X)
    loss=0
    for num in range(len(Y_Pred)):
        if Y_Pred[num]!=Y_true[num]:
            loss+=1
    only_loss[depth]=loss
only_loss_best=list(only_loss.keys())[list(only_loss.values()).index(min(only_loss.values()))]
print('If only consider zero-one loss, the best depth is:',only_loss_best)
    
error_nodes={}
for depth in range(1,6):
    clf=DecisionTreeClassifier(random_state =0,max_depth=depth)
    clf.fit(X, Y_true)
    Y_Pred = clf.predict(X)
    loss=0
    for num in range(len(Y_Pred)):
        if Y_Pred[num]!=Y_true[num]:
            loss+=1
    loss_node=loss+clf.tree_.node_count
    error_nodes[depth]=loss_node
all_loss_best=list(error_nodes.keys())[list(error_nodes.values()).index(min(error_nodes.values()))]
print('Consider both error and nodes, the best depth is:',all_loss_best)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            