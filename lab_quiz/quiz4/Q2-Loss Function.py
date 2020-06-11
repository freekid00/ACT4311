#coding=utf8
"""
Created on Thu Mar 12 17:48:23 2020

@author: Neal LONG

Hint max() is a built-in function in Python 
"""

import pickle

def linear_func(W,X):
    """
    General form of a 2-d linear function with w0 as intercept
    """
    return W[0]+W[1]*X[0]+W[2]*X[1]


def hinge_loss(f_x,y_true):
    """
    Compute the hinge loss given the returned value from 
        a linear discrimination function on the feature x and its label y 
    """
    return max(0,(1-f_x*y_true))
    

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
    
W = (-0.45236953,2.23604794, -3.94803128)
zero_one_loss_total = 0
for i in range(len(X)):
    x_i = X[i]
    f_x_i=linear_func(W,x_i)
    y_i = Y_true[i]
    loss = zero_one_loss(f_x_i,y_i)
    if loss > 0:
        print('error in {}-th case with f_x={} ,and y={}:'.format(i,linear_func(W,x_i),y_i))
    zero_one_loss_total+=loss
print("zero_one_loss_total of W is ",zero_one_loss_total)


W1 = (-0.762686,1.50126098,-2.3948365 )
W2 = (-0.422686,1.50126098,-2.3948365 )
W3 = (-0.59862686,1.50126098,-2.3948365)


#Compute zero_one_loss
all_W={'W1':(-0.762686,1.50126098,-2.3948365 ),
       'W2':(-0.422686,1.50126098,-2.3948365 ),
       'W3':(-0.59862686,1.50126098,-2.3948365)
       }
for W in all_W.values():
    zero_one_loss_total = 0
    for i in range(len(X)):
        x_i = X[i]
        f_x_i=linear_func(W,x_i)
        y_i = Y_true[i]
        loss = zero_one_loss(f_x_i,y_i)
        if loss > 0:
            print('error in {}-th case with f_x={} ,and y={}:'.format(i,linear_func(W,x_i),y_i))
            zero_one_loss_total+=loss
    print("zero_one_loss_total of W is ",zero_one_loss_total)
print('So for all W, the loss is 0')



#Compute hinge loss
all_W={'W1':(-0.762686,1.50126098,-2.3948365 ),
       'W2':(-0.422686,1.50126098,-2.3948365 ),
       'W3':(-0.59862686,1.50126098,-2.3948365)
       }
for W in all_W.values():
    hinge_loss_total = 0
    for i in range(len(X)):
        x_i = X[i]
        f_x_i=linear_func(W,x_i)
        y_i = Y_true[i]
        loss = hinge_loss(f_x_i,y_i)
        if loss > 0:
            hinge_loss_total+=loss
    print("hinge_loss_total of W is ",hinge_loss_total)
print('W2 min the hinge loss total')



















