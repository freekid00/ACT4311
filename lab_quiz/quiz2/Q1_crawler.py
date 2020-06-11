# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:02:26 2017

@author: Neal
shareholder information of a stock are listed in :
https://q.stock.sohu.com/cn/000001/ltgd.shtml
https://q.stock.sohu.com/cn/000002/ltgd.shtml
https://q.stock.sohu.com/cn/000003/ltgd.shtml
...
We want to know:
    1. which orgnizations hold most different number of sz50 listed companies

<tag_X class="val_a val_b"> content </tag_X> means tag_X has "class"  attribute with two values val_a and val_b
so tag_X can be find with beautifulsoup by selecting "class" attribute with value equal to either val_a or val_b
"""

import requests
from bs4 import BeautifulSoup
import csv
import time
import os
fake_header = {  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, sdch",
            "Accept-Language":"zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2"
        }

data_file= '/Users/zhangdi/ACT4311/lab_quiz/quiz2/stock_shareholders.csv'
#if not os.path.exists('./data'):
#    os.makedirs('./data')
    
sz50_stocks=('601989','601988','601985','601901','601881','601857','601818',
             '601800','601788','601766','601688','601668','601628','601601',
             '601398','601390','601336','601328','601318','601288','601229',
             '601211','601198','601186','601169','601166','601088','601006',
             '600999','600958','600919','600887','600837','600606','600547',
             '600519','600518','600485','600340','600111','600104','600100',
             '600050','600048','600036','600030','600029','600028','600016',
             '600000')

sz50_top10_stocks = sz50_stocks[:10]#only fetch top 10 stocks for quiz

#sz50_stocks=('601989','601988')
print('There are',len(sz50_top10_stocks), 'stocks in sz50_top5_stocks')

base_url = 'https://q.stock.sohu.com/cn/{}/ltgd.shtml' 
row_count = 0
#open file to with written permission 
with open(data_file,'w',newline='',encoding='utf8') as wf:
    writer = csv.writer(wf)
    for stock in sz50_top10_stocks:#process stock one by one
        #prepare the request webpage with desired parameters
        url = base_url.format(stock)
        print("Now we are crawling stock",stock)
        #send http request with fake http header
        response = requests.get(url,headers = fake_header)
        if response.status_code == 200:
            response.encoding = 'GBK'
            root = BeautifulSoup(response.text,"html.parser") 
            # search the table storing the shareholder information
            table = root.find('table',attrs={'class':'tableG'})
            # list all rows the table
            rows = table.find_all('tr')
            for row in rows: #iterate rows
                record=[stock,]# define an empty list to store columns of the row/record
                # list all columns of the row 
                columns = row.find_all('td')
                for col in columns: #iterate colums
                    record.append(col.get_text().strip())
                writer.writerow(record)
                
                if len(record)>1:# if has columns, save record to csv file using writer variable
                    #++insert your code here++
                    row_count+=1
        else:
            print('Failed to crawl the site for',stock)
        time.sleep(1)
print('Crawled and saved {} records of  shareholder information of sz50_top10 firms to{}'.format(row_count,data_file) )

shareholder_count=dict()
clean_rows=0
with open(data_file,'r',newline='',encoding='utf8') as rf:
    reader = csv.reader(rf)
    for row in reader:
        if len(row)!=7:
            continue
    #Then row is list of length 7, i.e., composed of 7 str elements as follows
    #row = [stock_code,inner_order,share_holder,shares_number,shares_percent,is_changed,changed_shares]
        share_holder = row[2]
        clean_rows+=1
        if share_holder not in shareholder_count:#first appearance, init the count with 1
            shareholder_count[share_holder]=1
        else:# existing shareholder in shareholder_count, add the count by 1
            shareholder_count[share_holder]+=1

print('We have processed {} valid rows from csv'.format(clean_rows))

sorted_shareHolder = sorted(shareholder_count.items(),key=lambda x:x[1],reverse=True)
print('The organization who hold maximum number sz50_top10 firms is {} and it holds {} SZ50 companies'.format(sorted_shareHolder[0][0],sorted_shareHolder[0][1]))

lines=0
for org,count in sorted_shareHolder:
    lines+=1
    if lines>10:
        break
    print(org,count)
    
            