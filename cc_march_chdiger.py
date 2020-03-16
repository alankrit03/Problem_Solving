# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 21:08:39 2019

@author: Alankrit_Agarwal
"""

# cook your dish here
t=int(input())
user_input_list=[]
for _ in range(t):
    user_input_list.append(input().split())
for user_input in user_input_list:
    
    d=user_input[1]
    list_num=list(user_input[0])
    n=len(list_num)
    i=0
    while(i<n):
        if(int(list_num[i]<=d)):
            i+=1
        else:
            list_num.pop(i)
            list_num.append(d)
    print(''.join(list_num))

import string
s=string.ascii_letters
print(s)