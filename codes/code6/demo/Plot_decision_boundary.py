#coding=utf8
"""
Created on Thu Mar 12 17:48:23 2020

@author: Neal LONG

Hint max() is a built-in function in Python 
"""

import pickle
import matplotlib.pyplot as plt
import numpy as np




    

def zero_one_loss(f_x,y_true):
    """
    Compute the zero-one loss given the returned value from 
        a linear discrimination function on the feature x and its label y
    """
    if f_x*y_true>=0:
        return 0
    else:
        return 1
    
with open('Q2_fetures.pkl','rb') as rf:
    X = pickle.load(rf)

with open('Q2_labels.pkl','rb') as rf:
    Y_true = pickle.load(rf)

print(len(X),len(Y_true))

def linear_func(W,X):
    """
    General form of a 2-d linear function with w0 as intercept
    """
    return W[0]+W[1]*X[0]+W[2]*X[1]
    
W = (-0.45236953,2.23604794, -3.94803128)
#f(x) = -0.45236953+2.23604794*X[0]-3.94803128*X[1] = 0
#        ->3.94803128*X[1] = -0.45236953+2.23604794*X[0]
#           y = (-0.45236953+2.23604794*x)/3.94803128

plt.figure(1, figsize=(8, 8))
plt.scatter(X[:, 0], X[:, 1], c=Y_true)

 #generate dense plots
s = np.arange(min(X[:, 0]),max(X[:, 0]),0.1)

#generate the corresponding y for each z in s
t = []
for z in s:
    t.append((-0.45236953+2.23604794*z)/3.94803128)
    
    
plt.plot(s, t)


zero_one_loss_total = 0
for i in range(len(X)):
    x_i = X[i]
    f_x_i=linear_func(W,x_i)
    y_i = Y_true[i]
    loss = zero_one_loss(f_x_i,y_i)
    if loss > 0:
        print('error in {}-th case with f_x={} ,and y={}:'.format(i+1,linear_func(W,x_i),y_i))
    zero_one_loss_total+=loss
print("zero_one_loss_total of W is ",zero_one_loss_total)


