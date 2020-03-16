# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 23:43:18 2019

@author: Alankrit Agarwal
"""
def fib(n):
    

    l=[0]*n
    l[1]=1
    for i in range(2,n):
        l[i]=l[i-2]+l[i-1]
    
    print(*l)
    
def fib_mod(n):
    l=[0]*n
    l[1]=1
    for i in range(2,n):
        l[i]=(l[i-2]+l[i-1])%10
    
    print(*list(enumerate(l)))