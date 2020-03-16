# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 11:14:56 2019

@author: Alankrit Agarwal
"""

import re

script='This$#is% Matrix#  %!'
print(script)
pat=r'(?<=\w)[!@#$%&\s]+(?=\w)'
print(re.findall(pat,script))
new_script=re.sub(pat,r' ',script)
print(new_script)

s1='This is Matrix#  %!'
s2='This is Matrix#  %!'
print(bool(s1==s2))
import numpy

print(numpy.roots([1,-5,6]))

print(globals())

