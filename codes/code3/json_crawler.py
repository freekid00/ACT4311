#coding=utf8
"""
Created on Thu Feb 20 00:53:28 2020

@author: Neal LONG
"""

import json
import requests
fake_header = {  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, sdch",
            "Accept-Language":"zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2"
        }

s = requests.Session()

r=s.get('https://xueqiu.com',headers = fake_header)
r = s.get('https://xueqiu.com/query/v1/symbol/search/status?u=401582129017261&uuid=1230174898194894848&count=10&comment=0&symbol=TSLA&hl=0&source=all&sort=&page=1&q=&session_token=null&access_token=b2f87b997a1558e1023f18af36cab23af8d202ea',headers = fake_header)

#print(r.text)
parsed_json1 = r.json
parsed_json2 = json.loads(r.text)

print(parsed_json2)
