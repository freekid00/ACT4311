#coding=utf8
"""
Created on Thu Sep 01 18:04:16 2019

@author: Neal LONG
"""

def calc_rect(height,width=5):
    perimeter = 2*(height+width)
    area = height*width
    return perimeter,area
print(calc_rect(3,2))
print(calc_rect(3))
print(calc_rect(width=4,height=2))
