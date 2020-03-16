# -*- coding: utf-8 -*-
"""
Created on Sun May 19 10:44:21 2019

@author: Alankrit Agarwal
"""
#This code is written to find at which testcase the solution is not working
#to directly get to it and not waste time finding the faulty testcase

inp=input("Enter the input data of the question:\n")

user_input=inp.split('\n')

print(user_input)
n=int(user_input.pop(0))

out1=input('Enter the output that is expected:\n')

exp_output=out1.split('\n')

act_output=input('Enter the output your code is giving:\n').split('\n')

for i in range(n):
    if exp_output[i]!=act_output[i]:
        print('Check out:\t{}\n'.format(user_input[i]))