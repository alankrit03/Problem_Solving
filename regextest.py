# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 19:38:01 2019

@author: Alankrit Agarwal
"""

import re
pat=r'(\d{4}-)(\d{4}-)(\d{4}-)\d{4}'
s='3456-63453455-3533'
pat2=r'(\d).\1'
print(re.search(pat2,s).group())
pat_not_allowed=re.compile(r'[^a-zA-Z0-9]' r'(.).\1' r'.{11,}')
print('chechk this')
print('chechk this again')
if re.search(r'[A-Z].*?[A-Z]','AhBYw9r675') and re.search(r'\d.*?\d.*?\d','AhBYw9r675'):
    print('this works')