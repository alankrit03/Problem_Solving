# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 13:54:09 2019

@author: Alankrit Agarwal
"""

def hcf(l,b):
    if l<b:
        l,b=b,l
    while(b):
        l,b=b,l%b
    
    return l