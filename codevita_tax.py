# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 10:07:29 2019

@author: Alankrit Agarwal
"""
def improvise(x):
  return int(x)/100


slab = list(map(int,input().split()))
rate = list(map(improvise,input().split()))
rebate = int(input())
tax = list(map(int, input().split()))

def cal_income(tax):
  if tax==0:
    return (slab[0]+rebate)
  
  pos=1
  edge=len(rate)
  income=slab[pos-1]
  while (tax):
      
    if edge == pos:
        income+= tax/rate[pos-1]
        return income+rebate
    
    inc_slab = slab[pos] - slab[pos-1]
    current_tax_slab = inc_slab*rate[pos-1]
    
    if current_tax_slab <= tax :
      print(pos)
      income = slab[pos]
      pos+=1
      tax-=current_tax_slab
    
    else:
      income+=tax/rate[pos-1]
      break
  
  return income+rebate

total_income=0
for x in tax:
  total_income+=cal_income(x)
  
print (total_income)