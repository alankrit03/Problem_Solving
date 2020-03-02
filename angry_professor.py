# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:23:27 2019

@author: Alankrit Agarwal
"""

#!/bin/python3


import os


# Complete the angryProfessor function below.
def angryProfessor(k, a):
    present=0
    for x in a:
        if x<=0:
            present+=1
    if present>=k:
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()