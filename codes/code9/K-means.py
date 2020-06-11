# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:24:09 2020

@author: Neal LONG
"""
#%%
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

iris = load_iris()
X, y = iris.data[:,:2], iris.target
km =KMeans(init='random', n_clusters=5,n_init=1)
labels = km.fit_predict(X)
case_idx = 12
print("The {}-th example in X is assigned to {}-th cluster".format(case_idx+1,
      labels[case_idx]+1))
#%%
    
runs = []
inertias_1_random = []
inertias_10_random = []
inertias_1_plus = []
inertias_10_plus = []
for run in range(10):
    runs.append(run)
    #========
    km =KMeans(init='random', n_clusters=5,n_init=1)
    km.fit(X)
    inertias_1_random.append(km.inertia_)
    #========
    km =KMeans(init='random', n_clusters=5,n_init=10)
    km.fit(X)
    inertias_10_random.append(km.inertia_)
    #========
    km =KMeans(init='k-means++', n_clusters=5,n_init=1)
    km.fit(X)
    inertias_1_plus.append(km.inertia_)
    #========
    km =KMeans(init='k-means++', n_clusters=5,n_init=10)
    km.fit(X)
    inertias_10_plus.append(km.inertia_)
#%%

for label, inertias in zip(("inertias_1_random","inertias_10_random","inertias_1_plus"
                            ,"inertias_10_plus"),(inertias_1_random,inertias_10_random,
                           inertias_1_plus,inertias_10_plus)):

    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(runs,inertias)
    plt.title("Internal distortions for KMeans with {}".format(label))
    plt.show()



