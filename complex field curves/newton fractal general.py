# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 16:17:20 2023

@author: sagar

This is a code to produce the newton's fractal for the equation x**3-1=0 

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.dpi']=500 # highres display

order=4
iteration=50

root=[]
for i in range(order):
    root.append(np.exp(1j*i*2*np.pi/order))


roots=len(root)
colors=np.linspace(0,1,order)

def f(z):
    val=z**order-1
    return(val)

def df(z):
    val=order*z**(order-1)
    return(val)

x=np.linspace(-1,1,1001)
y=np.linspace(-1,1,1001)

X,Y=np.meshgrid(x,y)
z=X+Y*1j
output=np.zeros(z.shape)

for i in range(iteration):
    z=z-f(z)/df(z)
    
    
def colour(z):
    global output
    for i in range(z.shape[0]):
        for j in range(z.shape[1]):
            dist=[]
            for k in range(roots):
                dist.append(abs(z[i,j]-root[k]))
                print(z[i,j])
                print(dist)
            try:
                nearest=np.where(dist==np.min(dist))[0][0]
            except:
                #print(z[i,j])
                nearest=0
            output[i,j]=colors[nearest]

colour(z)

plt.imshow(output)
plt.axis('off')
plt.show()

print(output)