# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:51:48 2019

@author: Alankrit Agarwal
"""

regex_integer_in_range = r"[1-9]\d{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

print(re.match(regex_integer_in_range, P))
print(re.findall(regex_alternating_repetitive_digit_pair, P))

pat=r'#[0-9a-fA-F]{6}'
s='color: #FfFdF8; background-color:#aef;'
print(re.findall(pat,s))    


def test(n1,n2):
    return n1+n2