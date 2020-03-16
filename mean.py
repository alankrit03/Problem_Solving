# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 11:59:28 2019

@author: Alankrit Agarwal
"""

#calculating mean of a series

data=list(map(int,input().split(', ')))

total=0

for x in data:
    total+=x
    
mean=(total/len(data))
print('mean=',mean)


sq_diff=[(x-mean)**2 for x in data]

var=0
for x in sq_diff:
    var+=x
    
print('variance=',var/len(data))

print('standard deviation=',(var/len(data))**0.5)