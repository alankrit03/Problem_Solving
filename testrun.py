# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 19:10:51 2019

@author: Alankrit Agarwal
"""
import re
m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<exteon>\w+)','alankrit@hackerrank.com')
print(m.groupdict())
lst=re.fullmatch
s='alankrit'
pat=r'al'
t=re.sub(pat,'new',s)
print(s,t,sep='\n')

def test():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    import re
    for _ in range(int(input())):
        s=input()
        not_allowed_char=r'[^0-9-]'
        if re.search(not_allowed_char,s):
            print("Invalid")
        else:
            nor_pat=r'^[456]{1}[0-9]{15}' #checking for normal code without any dashes
            if re.search(nor_pat,s):
                if re.search(r'(\d)\3{4,}',s):
                    print("Invalid")
            else:
                pass
    
            print("VAl")

pattern = r"Cookie"
sequence = "Cooki8e7"
if re.match(pattern, sequence):
  print("Match!")
else: print("Not a match!")

