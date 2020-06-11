# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 10:53:01 2018

@author: Neal

Now we need to identify all odd in the tuple all_numbers, and
compute the mean value of all identified odd numbers and these unique
identified odd numbers
"""
import numpy
all_numbers = (103,119,119,150,151,159,111,139,149,103,101,103,101,101,117,136,133,
 122,122,139,141,145,135,112,133,112,106,127,116,101,100,125,100,102,139,111,123,
 150,146,109,149,142,150,132,146,103,107,101,110,101,135,141,100,115,105,139,134,
 136,122,145,127,120,108,137,137,111,150,109,122,120,113,134,138,138,108,141,108,
 108,104,147,124,137,117,101,136,143,147,126,125,120,142,102,145,135,115,105,101,
 103,145,150,100,118,128,123,133,342,6,4,323,6,54324,7,34,37,34,76,546,34)


all_odds=[]
for i in all_numbers:
    if i%2==1:
        all_odds.append(i)
print(all_odds)

unique_odds=[]
for i in all_odds:
    if i not in unique_odds:
        unique_odds.append(i)
print(unique_odds)

print('The mean value of all odd numbers stored in tuple all_numbers is', numpy.mean(all_odds))
print('The mean value of unique odd numbers stored in tuple all_numbers is', numpy.mean(list(unique_odds)))