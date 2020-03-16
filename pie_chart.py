# -*- coding: utf-8 -*-
"""
Created on Sat May 18 22:19:54 2019

@author: Alankrit Agarwal
"""


from random import sample
import matplotlib.pyplot as plt
import matplotlib.colors as pltc

populations=[1420,1368,329,269,212,204]

colors = sample(list(pltc.cnames.values()) , len(populations))

#

country= ['China', 'India' , 'US', 'Indonesia', 'Brazil', 'Australia' ]

space_slice= [0.05 , 0 ,0,0,0,0]

plt.figure(figsize=(6,5))

plt.pie(populations, labels=country, autopct='%1.1f%%',
        shadow=False, explode=space_slice,colors=colors)

plt.legend(country , loc=(-0.25 , 0.7) , shadow=True)

plt.show()