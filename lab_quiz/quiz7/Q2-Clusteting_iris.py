#coding=utf8
"""
Created on Wed Nov 08 17:51:36 2017

@author: Neal LONG
Now you need to cluster the iris data using KMeans with n_init=100 and 'k-means++'
for initialization and try different cluster numbers from 2 to 10, i.e.,  
(2,3,4,...,10),and :
    1. Determine which cluster number will give you minimum clustering distortion(inertia), 
        and in the correspongding clustering results, report whether the 
        3-rd example and 4-th example clustered into same group
        (please note the correct position index) 
        
    2. By comparing the distortion of clustering with different cluster numbers,
       answer that when the number of clusters increases, how will the distortion
       of clustering will change(increase,decrease or it depends)
       
Please note that the n_init of KMeans should be increased to 100 for stable answer
"""


from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np 
iris = load_iris()
X, y = iris.data, iris.target

#++insert your code below++

cluster_list=np.arange(2,11)
inertias=[]
for cluster_num in cluster_list:
    km =KMeans(init='k-means++', n_clusters=cluster_num,n_init=100)
    km.fit(X)
    inertias.append(km.inertia_)
fig=plt.figure()
ax = plt.axes()
ax.bar(list(cluster_list),inertias)
plt.show()
print('so the best estimator for cluster num is 10')

km =KMeans(init='k-means++', n_clusters=10,n_init=100)
results=km.fit_predict(X)
results=results[2]==results[3]
print('Whether 3rd is equal to 4th?',results)





