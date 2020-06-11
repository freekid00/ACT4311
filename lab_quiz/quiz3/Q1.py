# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 23:01:16 2020

@author: Neal LONG

Interate the 9 posts in the 'SZ000063.json' downloaded from Xueqiu,
and count how many times in total the word "5G" apears in the 'text' attribute
of the 9 posts


Hint: use count method for string (type/class)
"""

import json

with open('/Users/zhangdi/ACT4311/lab_quiz/quiz3/SZ000063.json',encoding='utf8') as rf:
    xueqiu_json = json.load(rf)

print(type(xueqiu_json['list']),len(xueqiu_json['list']))

# Fetch the id of 2nd post
print("The id of second post is", xueqiu_json['list'][1]['id'])


#Write your code below
with open('/Users/zhangdi/ACT4311/lab_quiz/quiz3/SZ000063.json',encoding='utf8') as rf:
    xueqiu_json = json.load(rf)
    count=0
    for i in range(9):
        count+=xueqiu_json['list'][i]['text'].count('5G')
    print(count)