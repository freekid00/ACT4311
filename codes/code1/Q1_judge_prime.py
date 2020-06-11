# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 19:06:05 2019

@author: Neal
"""

"""
Judge the positive integer number in num_to_check is whether a prime number

A prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

a%b return remainder of a divided(integer division) by b
so 2%3=5%3=11%3=2
then if a%b==0 we could b is a divisor of a 
"""

num_to_check=63
# is_prime is set to be true by default
is_prime = True
for smaller_int in range(2,num_to_check):
   if  #++insert your code here++ to judge whether num_to_check is not prime
        #++ update is_prime to False if num_to_check is not prime++
        print(smaller_int)
        break
print('num_to_check is prime?',is_prime)
    