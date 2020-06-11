#coding=utf8
"""
Created on Thu Apr 23 01:56:33 2020

@author: Neal LONG
"""

#%%
import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer
import numpy as np
from sklearn.metrics import accuracy_score



class NB():
    
    def fit(self, df, y):
        """
        Accumulate the count for class prior and individual joint event
        """
        self.event_count_dict = dict()
        self.prior_count_dict =  dict()
        self.attrs = df.columns # names of attributes
        self.size= 0 # number of observations
        
        # Update count of individual observations
        for attr in self.attrs:
            for attr_val,label in zip(df[attr],y):
                event = '{}={}'.format(attr,attr_val)
                if (event,label) in self.event_count_dict:
                    self.event_count_dict[(event,label)] +=1
                else:
                    self.event_count_dict[(event,label)] =1
                    
        # Update count of class priors     
        for label in y:
            self.size+=1
            if label in self.prior_count_dict:
                    self.prior_count_dict[label] +=1
            else:
                self.prior_count_dict[label] =1
            


    def conditional_proba(self, attr,attr_val,label):
        """
        Compute the  conditional probability
        """
        event = '{}={}'.format(attr,attr_val)
        joint_event_count = self.event_count_dict.get((event,label),0)
        class_prior = self.prior_count_dict[label]
        return joint_event_count/class_prior
    
    def predict(self, X):
        """
        Predict the class labels for M example in X, the feature vector of 
        each examle is similar to df during fit
        """

        labels = []
        for vec in X:
            cp_yes=1
            cp_no=1
            for attr,attr_val in zip(self.attrs,vec):
                cp_yes=cp_yes*self.conditional_proba(attr,attr_val,'yes')
                cp_no=cp_no*self.conditional_proba(attr,attr_val,'no')
            cp_yes=cp_yes*self.prior_count_dict['yes']/(self.prior_count_dict['yes']+self.prior_count_dict['no'])
            cp_no=cp_no*self.prior_count_dict['no']/(self.prior_count_dict['yes']+self.prior_count_dict['no'])
            if cp_yes>=cp_no:
                labels.append('yes')
            else:
                labels.append('no')
            """
            predict the label for each vec and apppend to list labels as follows
          
                Step 1. you can use following instructions to generate each 
                       joint event :
                         "for attr, attr_val in zip(self.attrs,vec): " 
                Step 2. you can use function conditional_proba to compute the
                        conditional probability of each joint event, P(e1|c)  
                Step 3. Compute the joint probability P(E|c)*P(C) of for each 
                        label of a given example with Naive assumptions,
                        and then predict the label by comarison
                Hint: 
                    1. dict.items() can used to iterate key-value pairs
                    2. sorted function can be used for picking the most likely label
                
                        
            """  

            
        return labels
    
    
#======Application of defined NB model    
df = pd.read_csv('golf.csv')
print(df)    

kbd = KBinsDiscretizer(3,encode='ordinal')
df[['Temperature','Humidity']] = kbd.fit_transform(df[['Temperature','Humidity']])
print("\nAfter feature engineering:")
print(df)   
y = df.pop('Play')
clf = NB()                                                   
clf.fit(df,y)  
pred_labels = clf.predict(df.values)
mean_acc = np.mean(accuracy_score(pred_labels, y))

print("\nApplication Results:")
print("The average accuracy score on training data of NB is", mean_acc)



# %%
