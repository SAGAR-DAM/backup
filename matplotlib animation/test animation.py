# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 22:25:43 2023

@author: sagar
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#import matplotlib
#matplotlib.rcParams['figure.dpi']=300 # highres display

xdata=np.linspace(-5,5,200)

x=[]
y1=[]
y2=[]

plt.figure(figsize=(40,30))

def animate(i):
    x.append(xdata[i])
    y1.append(np.sin(xdata[i]))
    y2=np.random.uniform(low=np.min(x),high=np.max(x),size=len(x))
    
    plt.clf()
    plt.plot(x,y1)
    plt.plot(x,y2,'ko')
    
ani=FuncAnimation(plt.gcf(),animate, range(0,len(xdata)-1), interval=1, repeat=False)

plt.show()