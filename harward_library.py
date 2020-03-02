# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:54:23 2019

@author: Alankrit Agarwal
"""

if __name__=="__main__":
  input()
  d=input().split('~')
  books={}
  
  while(d[0]!='Borrowers'):
    books[d[0]]=d[1]
    d=input().split('~')
  
  d=input().split('~')
  borrower={}
  
  while(d[0]!='Checkouts'):
    borrower[d[0]]=d[1]
    d=input().split('~')
  
  d=input().split('~')
  checkout={}
  while(d[0]!='EndOfInput'):
    checkout[d[0]]=d[1:]
    d=input().split('~')