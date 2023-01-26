# -*- coding: utf-8 -*-
"""
Created on Fri May 20 19:26:59 2022

@author: mrsag
"""

'''PROBLEM 10 WITH NUMPY FFT MODULE
SAGAR DAM;  DNAP'''

import numpy as np
import matplotlib.pyplot as plt

#initializing variables
r=[0.01,0.04,0.05]
aaa=0
def f(t):
   if(abs(t)<=0.01):
       z=100
   else:
       z=0
   return z
'''def f(t):
    if(t==1):
        z=5000
    else:
        z=0
        
    return z'''
for q in range(3):
    

    a=10000
    h=r[q]
    x=np.arange(-a,a,h)
    g=np.zeros(len(x))
    for j in range(len(x)):
        g[j]=f(x[j])
    sp = np.fft.fft(g)
    freq = np.fft.fftfreq(x.size)*2*np.pi/h
    sp*=h*np.exp(-complex(0,1)*freq*(a))/(np.sqrt(2*np.pi))
    if(h==r[0]):
        plt.plot(freq,sp,'r',label='FT with real spacing=0.1')
    elif(h==r[1]):
        aaa=0
        #plt.plot(freq,sp,'g',label='FT with real spacing=0.4')
    else:
        aaa=0
        #plt.plot(freq,sp,'b',label='FT with real spacing=0.5')

p=np.arange(-10,10,0.1)
sinc=np.zeros(len(p))
box=np.zeros(len(p))

def true(t):
    if(t==0):
        z=1
    else:
        z=np.sin(t)/t
    return(z*np.sqrt(2/np.pi))
for i in range(len(p)):
    sinc[i]=true(p[i])
    box[i]=f(p[i])
    
#plt.plot(p,box,color='violet',label='box function')
#plt.plot(p,sinc,'ko',markersize=1,label='analytical FT')
plt.legend()
plt.title('FT of box function with numpy module for 3 different sampling rate')
plt.grid()
plt.gca().set_xlim(-100,100)
plt.show()
