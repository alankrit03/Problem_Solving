# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:22:12 2019

@author: Alankrit Agarwal
"""

def function_interval(array):
    ans=[array[0][0]]
    current_ele=array[0][1]
    n=len(array)
    for i in range(1,n):
        if current_ele<array[i][0]:
            ans.extend([current_ele,array[i][0]])
            current_ele=array[i][1]
        elif current_ele>=array[i][0] and current_ele<=array[i][1]:
            current_ele=array[i][1]
    else:
        ans.append(current_ele)
    return ans
    print('array',array)
    
        


for _ in range(int(input())):
    size=int(input())
    data=input().split()
    for i in range(len(data)):
        data[i]=int(data[i])
        
    clean_data=[]
    for i in range(0,len(data),2):
        clean_data.append([data[i],data[i+1]])
    clean_data.sort(key=lambda x:x[0])
    
    
    ans=function_interval(clean_data)
    
    data=[item for items in clean_data for item in items]
    
    
    #print(clean_data)
    #print(data)
    print(*ans)