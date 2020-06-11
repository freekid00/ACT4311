# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 23:51:04 2020

@author: Neal LONG
"""

class Person:
    
    def __init__(self, input_name, input_age):
        self.name = input_name
        self.age = input_age

    def myfunc(self):
        print("Hello my name is " + self.name)
        

p1 = Person("John", 36)
#    1. self = Person Object but empty
#    2. __init__(self, "John", 36)
#    3. return self to p1 , p1 = self
p1.myfunc()
print(p1.age)

p2 = Person("Jim", 22)
p2.myfunc()
