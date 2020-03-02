# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:52:53 2019

@author: Alankrit Agarwal
"""

T=int(input())

for _ in range(T):
    n=int(input())
    data=input().split()
    total=0
    for i in range(n):
        data[i]=int(data[i])
        total+=data[i]
    data_mean=total/n
    #print(data_mean)
    for i in range(n):
        if data[i]==data_mean:
            print(i+1)
            break
    else:
        print('Impossible')