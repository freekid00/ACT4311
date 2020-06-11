# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 16:21:46 2018

@author: Neal
"""

import pickle
data_path = './data/dict.pkl'

# An arbitrary collection of objects supported by pickle.
data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", "byte string"),
    'c': {None, True, False}
}

print("==Data dumped to pickle==")
print(data)
with open(data_path, 'wb') as wf: 
    # Pickle the 'data' dictionary
    pickle.dump(data, wf) 

print("==Data loaded from pickle==")    
with open(data_path, 'rb') as rf:
    # Load the 'data' dictionary back from pickle
    data_new = pickle.load(rf)  
print(data_new)