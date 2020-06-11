# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:43:01 2020

@author: Neal LONG
"""
#%%
#Import Library of Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB
import numpy as np

print("\n")
print('Train model_1 with first 8 and then remaining 4 training examples')
print("#"*30)


#assigning predictor and target variables
X= np.array([[-3,7],[1,5], [1,2], [-2,0], [2,3], [-4,0], [-1,1], [1,1], [-2,2], [2,7], [-4,1], [-2,7]])
y = np.array([3, 3, 3, 3, 4, 3, 3, 4, 3, 4, 4, 4])
#Create a Gaussian Classifier model_1
model_1 = GaussianNB()

# Train the model_1 with the first 8 training examples 
model_1.fit(X[:8], y[:8])

#Predict output with model_1 trained on first 8 training examples
print("Predict output with model_1 trained on first 8 training examples:")
print( model_1.predict([[1,2],[2,3]]))

# Further train model_1 with the remaining training examples from the 9th examples
model_1.partial_fit(X[8:], y[8:])

#Predict output with newly partially trained model_1
print("Predict output with newly partially trained model_1:")
print(model_1.predict([[1,2],[2,3]]))


print("\n")
print('Train model_2 with 12 total training exaples once')
print("#"*30)

#Create a Gaussian Classifier model_2
model_2 = GaussianNB()

# Train the model_1 with 12 total training exaples once
model_2.fit(X, y)

#Predict output with model_2
print("Predict output with model_2:")
print(model_2.predict([[1,2],[2,3]]))
#%%