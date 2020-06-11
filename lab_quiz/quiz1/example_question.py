#coding=utf8
"""
Created on Mon Sep 11 23:13:40 2018

@author: Neal LONG
"""

long_str= 'abcbdbabdbabbbbdsbbcbdbfsfdsgjhgksfdgfhghgfapsdncxvnowqqwertyuiopasdfghjkmnbzsbabdbcbsbd'
char_freq=dict()
for char in long_str:
    if char not in  char_freq: #accumulate,add the frequency of current character by 1
        #insert your code here #
        char_freq[char]=1
    else: #first occurance, set the frequency of current character to be 1
        #insert your code here #
        char_freq[char] += 1

print("Iterate keys")
for char in char_freq:
    print(char)

print("Iterate (key,value) pairs")
for (char,freq) in char_freq.items():
    print(char,'appears',freq,'times in long_str')

#sort the char by freq    
sorted_char_freq = sorted(char_freq.items(),key=lambda item:item[1], reverse=True)
char_freq_3rd = sorted_char_freq[2]
print(char_freq_3rd[0],'is the 3rd most frequent char, and appear',char_freq_3rd[1],'times in long_str')