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

omega=(-1+np.sqrt(3)*1j)/2

root=[1,-1,1j,-1j]
iteration=20

roots=len(root)


def f(z):
    val=z**4-1
    return(val)

def df(z):
    val=4*z**3
    return(val)

x=np.linspace(-1,1,2001)
y=np.linspace(-1,1,2001)

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
            if(nearest==0):
                output[i,j]=0
            elif(nearest==1):
                output[i,j]=0.33
            elif(nearest==2):
                output[i,j]=0.67
            elif(nearest==3):
                output[i,j]=1

colour(z)

plt.imshow(output)
plt.axis('off')
plt.show()

print(output)