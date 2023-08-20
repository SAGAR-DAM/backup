# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 18:44:34 2023

@author: sagar
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.dpi']=300 # highres display

hilbert=[]
vonkoch=[]
branching=[]

maxval=10
index=np.arange(0,maxval)
for i in range(0,maxval):
    x=5*4**i+7*(4**i-1)/3
    hilbert.append(x)
    print(int(x))
    
for i in range(0,maxval):
    x=(2**(2*i+1)-1)*3+2
    vonkoch.append(x)
    print(int(x))
    
for i in range(0,maxval):
    x=(2*5**i-1)*2+1
    branching.append(x)
    print(int(x))
    
plt.title("computational complexity of fractals")
plt.plot(index,vonkoch,'ro-',label='Von-Koch')
plt.plot(index,hilbert,'ko-',label='Hilbert')
plt.plot(index,branching,'bo-',label='Branching')
plt.legend()
plt.show()

hilbert_len=[]
vonkoch_len=[]
branching_len=[]

for i in range(0,15):
    y=(4*4**i-1)*600/(3*2**i)
    hilbert_len.append(y)
    
    y=3*(4/3)**i*600
    vonkoch_len.append(y)
    
    y=2*(5/3)**i*600
    branching_len.append(y)
    
print(hilbert_len)
print(vonkoch_len)

plt.plot(hilbert_len,'ro-',label='Hilbert length')
plt.plot(vonkoch_len,'bo-', label='Von-Koch length')
plt.plot(branching_len,'go-',label='Branching length')
plt.title("Length comparisn vs steps")
#plt.yscale('log')
plt.legend()
plt.show()
    