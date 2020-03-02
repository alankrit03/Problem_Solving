# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 23:16:58 2019

@author: Alankrit Agarwal
"""

import os

def count_min_op(old,new):
    pos=0
    len_old=len(old)
    len_new=len(new)
    
    while pos<len_new and pos<len_old:
        if old[pos]==new[pos]:
            pos+=1
        else:break
    
    return len(old[pos:]) + len(new[pos:]) , len_old , len_new

# Complete the appendAndDelete function below.

def appendAndDelete(s, t, k):
    min_op,len_s,len_t=count_min_op(s,t)
    #print(s,t,k)
    #print(min_op)
    if k>len_s+len_t:
        return 'Yes'
    
    if min_op:
        if min_op>k:
            return 'No'
        elif min_op==k or (k-min_op)%2==0: 
            return 'Yes'
        else:return 'No'
    else:
        if (k-min_op)%2==0:
            return 'Yes'
        else:return 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()