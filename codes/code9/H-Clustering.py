# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 19:13:45 2020

@author: Neal LONG
"""
#%%
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
iris = load_iris()
X = iris.data

print('\n',"="*40)
print("When distance threshold =0")
# setting distance_threshold=0 ensures we compute the full tree.
model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)
labels = model.fit_predict(X)
print(labels,len(set(labels)))
#%%
print('\n',"="*40)
print("When distance threshold =1")
model = AgglomerativeClustering(distance_threshold=1, n_clusters=None)
labels = model.fit_predict(X)
print(labels,len(set(labels)))
#%%
print('\n',"="*40)
print("When  n_clusters =25")
model = AgglomerativeClustering(n_clusters=25)
labels = model.fit_predict(X)
print(labels,len(set(labels)))
#%%

print('\n',"="*40)
print("When  n_clusters =3")
model = AgglomerativeClustering(n_clusters=3)
labels = model.fit_predict(X)
print(labels,len(set(labels)))


# %%
