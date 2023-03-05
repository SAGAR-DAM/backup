# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 22:59:03 2023

@author: sagar
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


x=np.arange(0,100)
y=3*x+10

for i in range(len(y)):
    y[i] += np.random.randint(0,10)

def straightline(x, A, B): # this is your 'straight line' y=f(x)
    return A*x + B

def linefit(x,y):
    x=np.array(x)
    parameters,pcov = curve_fit(straightline, x,y, maxfev=100000) # your data x, y to fit
    line=straightline(x,*parameters)             
    return(line,*parameters)               

line,*parameters=linefit(x,y)

plt.plot(x,y,'ro',label='data')
plt.plot(x,line,'k-',label='fit')
plt.xlabel("Slope: %f"%parameters[0] +"    offset: %f"%parameters[1])
plt.legend()
plt.show()
