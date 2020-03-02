# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:26:18 2019

@author: Alankrit Agarwal
"""

#!/bin/python3

import os

#Complete the kangaroo function below.

def kangaroo(x1, v1, x2, v2):
    
    distance_diff = x2-x1
    speed_diff = v2-v1
    
    print(distance_diff)
    print(speed_diff)
    
    if distance_diff*speed_diff>0:
        return 'NO'
    if distance_diff and not speed_diff:
        return 'NO'
    speed_diff=abs(speed_diff)
    if distance_diff%speed_diff:
        return 'NO'
    else : return 'YES'
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()