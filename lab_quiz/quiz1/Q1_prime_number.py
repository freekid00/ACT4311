# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 19:03:32 2018

@author: Neal
"""

"""
Please count the number of prime number between 600 and 700(include)
A prime number (or a prime) is a natural number greater than 1 that has no
positive divisors other than 1 and itself.

a%b return remainder of a divided(integer division) by b
so 2%3=5%3=11%3=2
then if a%b==0 we could b is a divisor of a 

"""

def judge_prime(num_to_check):
    is_prime = True
    for smaller_int in range(2,num_to_check):
       if  num_to_check%smaller_int==0:
            is_prime=False
            print('The first divisor for {} is {}'.format(num_to_check,smaller_int))
            break
    return is_prime

prime_count=0
for num_to_check in range(8000,9001):
    is_prime=judge_prime(num_to_check)
    if is_prime:
        prime_count+=1

print('There are',prime_count,'prime numbers between 8000 and 9000(both inclusive)')