# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 23:51:04 2020

@author: Neal LONG
"""

class Person:
    class_attr = "person"
    
    def __init__(self, input_name, input_age):
        self.name = input_name
        self.age = input_age

    def myfunc(self):
        print("Hello my name is " + self.name)
        
    def class_func():
        print("Hello World")

p1 = Person("John", 36)
p1.myfunc()
print(Person.class_attr)
print(p1.class_attr)
Person.class_func()
# No Person.myfunc()
# No p1.class_func()