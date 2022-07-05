# -*- coding: utf-8 -*-
"""
Created on Wed May 18 18:37:08 2022

@author: mrsag
"""
import numpy as np
from matplotlib import pyplot as plt
import scipy.integrate as integrate
#######################################################

limit=20
N=1000*2
times=np.linspace(-limit,limit,N)

#######################################################

def Si_integrand(t):
    f1=np.sin(np.pi*t**2/2)
    return f1
  
def Si(x):
    Isin=integrate.quad(Si_integrand,0,x)
    return Isin

######################################################

def Co_integrand(t):
    f2=np.cos(np.pi*t**2/2)
    return f2
  
def Co(x):
    Icos=integrate.quad(Co_integrand,0,x)
    return Icos


sinarray=[]
cosarray=[]
for i in range(len(times)):
    x1=Si(times[i])
    x2=Co(times[i])
    sinarray.append(x1)
    cosarray.append(x2)
    
plt.plot(cosarray,sinarray,'r-')
plt.show()