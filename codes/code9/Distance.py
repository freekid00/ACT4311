#coding=utf8
"""
Created on Wed Apr  1 23:34:19 2020

@author: Neal LONG
"""
# %%
from sklearn.neighbors import DistanceMetric
from math import sqrt
from numpy import argmin
print(sqrt(27),sqrt(108))
dist = DistanceMetric.get_metric('euclidean')
X = [[0, 1, 2],
      [3, 4, 5]]

Y = [[0, 1, 2],
     [3, 4, 5],
     [6, 7, 8]]

Z=[[0, 1, 2]]
# %%

print("====\nPairwise euclidean distance between X and X is:")
print(dist.pairwise(X))
# %%

print("====\nPairwise euclidean distance between X and Y is:")
print(dist.pairwise(X,Y))
# %%

print("====\nPairwise euclidean distance between X and Z is:")
print(dist.pairwise(X,Z))
# %%

idx = argmin(dist.pairwise(X,Y)[0])
print("====\nNeareat neighbors for the 1st example in X among Y is Y[{}] = {}".format(
        idx,Y[idx]))

idx = argmin(dist.pairwise(Y,X)[2])
print("====\nNeareat neighbors for the 3rd example in Y among X is X[{}] = {}".format(
        idx,X[idx]))



# %%
