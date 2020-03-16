# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 19:26:24 2019

@author: Alankrit Agarwal
"""

# snippet to find the prime number

def isprime(x):
    if x==2 or x==3:
        return True
    if x%2==0 or x%3==0:
        return False
    for i in range(5,int(x**0.5)+1,2):
        if x%i==0:
            return False
    else:return True