# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 19:05:16 2020

@author: Neal LONG

Complete the definition of a KNN model Class with Euclidean distance, 
    then build a KNN model with k=5,
    train the model on Iris data, finally apply it to predict the label
    and probability of a given test example with feature vector = [1,2,3,4]
"""

from sklearn.datasets import load_iris
from sklearn.neighbors import DistanceMetric
import pandas as pd
import numpy as np
iris = load_iris()

class KNN():
    def __init__(self, k=2):
        self.k = k
        self.dist = DistanceMetric.get_metric('euclidean')
    
    def fit(self,X,y):
        """
        Train a KNN model on training data is just simply keep the data
        Assume that the X is n*d matrix(n examples, and d dimension feature), 
                        and y is one array of n labels
        """
        if X.shape[0] != len(y):
            print("Error: number of training features does not match labels!")
            return
        self.X = X
        self.y = y 
        
    def predict_proba(self, X_new):
        """
        Predict the lables and probabilties of the feature nmatrix of m new 
        examples in X_new, its dimension should be same to self.X.
        You are supposed to use self.dist to compute the distance, and then 
        select K nearest neighbors. The weight for selected K neighbors is determined 
        by the inverse of their squared distance (as in lecture), repectively
        Hint: 
            1. you may use sorted function together with zip function
                OR jusr use numpy.argmin to select K nearest neighbors
            2. you may use dict to accumulate scores of labels among K nearest neighbors
            3. you may sorted function to determine the final predicted label
                and probability 
            4. The weight for selected K neighbors is determined by the inverse of their squared distance 
            
        
        """
        if X.shape[1] != len(X_new[0]):
            print("Error: dimension of testing features does not match training data!")
            return
        label_probs = [] 
        # store the predict label and probability for every example in X_new
        # example of label_probs for X_new with 3 examlples like [(1,0.983),(0,0.769),(0,0.457)]
        # means that the predicted label for 1st case is 1 and the probability is 0.983
        #            the predicted label for 2nd case is 0 and the probability is 0.769
        #            the predicted label for 3rd case is 0 and the probability is 0.457
        
        
        #++insert your code below to compute and fill label_probs ++
        label_probs=[]
        for instance in X_new:
            instance=np.array([instance])
            self.distance=self.dist.pairwise(instance,self.X)
            self.distance_weight_matrix=1/(np.array(list(self.distance[0])))**2
            self.weight_label=pd.DataFrame({'weight':self.distance_weight_matrix,'label':self.y})
            self.weight_label=self.weight_label.sort_values('weight',ascending=False,ignore_index=True).iloc[:self.k,:]
            self.weight_sum=np.sum(self.weight_label['weight'])
            self.label_choose=self.weight_label.groupby('label').aggregate({'weight':sum}).reset_index()
            self.label_choose['weight_sum']=self.weight_sum
            self.label_choose=self.label_choose.eval('probability=weight/weight_sum').sort_values('probability',ascending=False).iloc[0]
            self.result=(int(self.label_choose['label']),self.label_choose['probability'])
            label_probs.append(self.result)
        return  label_probs
    

X, y = iris.data, iris.target

knn_clf = KNN(5)
knn_clf.fit(X,y)
label_probs =knn_clf.predict_proba([[1,2,3,4],[2,3,4,5]])
print('for vector first')
label, prob = label_probs[0]
print("Label={}, with probability = {}".format(label,prob))


