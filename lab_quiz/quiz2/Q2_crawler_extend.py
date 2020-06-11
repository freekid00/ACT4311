# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:50:39 2018

@author: Neal
Based on the crawled results in Q2, now we want to know
which orgnizations hold most percentage of shares for sz50_top10 listed companies
"""
import csv
data_file= '/Users/zhangdi/ACT4311/lab_quiz/quiz2/stock_shareholders.csv'

shareholder_percent=dict()

with open(data_file,'r',newline='',encoding='utf8') as rf:
    reader = csv.reader(rf)
    for row in reader:
        if len(row)!=7:
            continue
        share_holder = row[2]
        shares_percent = float(row[3])
        if share_holder not in shareholder_percent:
            shareholder_percent[share_holder]=shares_percent
        else:
            shareholder_percent[share_holder]+=shares_percent
        
total=sum(shareholder_percent.values())
for key,value in shareholder_percent.items():
    shareholder_percent[key]=shareholder_percent[key]/total
sorted_shareHolder = sorted(shareholder_percent.items(),key=lambda x:x[1],reverse=True)
lines=0
for item in sorted_shareHolder:
    lines+=1
    if lines>10:
        break
    print(item[0],item[1])