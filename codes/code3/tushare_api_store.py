#coding=utf8
"""
Created on Thu Sep  5 11:02:00 2019

@author: Neal LONG

https://tushare.pro/document/2?doc_id=27
"""

import tushare as ts



#（your token可以在免费注册后，个人主页的“接口Token”下找到）
api = ts.pro_api("4f23ab6dc1ba48881847847915f2d04fac4ebdeb03ef153537ddf2ca")

result = api.daily(ts_code='000001.SZ', start_date='20200214', end_date='20200220')
result.to_excel('sz000001.xlsx')