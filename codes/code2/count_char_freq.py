#coding=utf8
"""
Created on Mon Sep 11 23:13:40 2018

@author: Neal LONG
"""

long_str= 'abcbdbabdbabbbbdsbbcbdbsbabdbcbsbd'
char_freq=dict()
for char in long_str:
    if char not in  char_freq: 
        char_freq[char]=1
    else:  
        char_freq[char]+=1
print("Iterate keys")
for char in char_freq:
    print(char)
print("Iterate (key,value) pairs")
for char,freq in char_freq.items():
    print(char,'appears',freq,'times in long_str')
