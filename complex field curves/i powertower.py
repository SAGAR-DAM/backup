# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 09:22:31 2023

@author: sagar
"""

import matplotlib.pyplot as plt
import numpy as np

import matplotlib
matplotlib.rcParams['figure.dpi']=300 # highres display

def power_tower(x,n):
    if n==0:
        return x**0
    else:
        return(x**power_tower(x, n-1))
    
    
reals=[]
imgs=[]

for i in range(0,200):
    z=power_tower((0+1j), i)
    print(z)
    reals.append(z.real)
    imgs.append(z.imag)
    
plt.plot(reals,imgs,'ko')
plt.title("Power tower of i in complex plane:   "+r"z=$i^{i^{i^{...^{i}}}}$", fontname='Times New Roman')
plt.xlabel("Re(z)",fontname='Times New Roman')
plt.ylabel("Im(z)",fontname='Times New Roman')
plt.show()