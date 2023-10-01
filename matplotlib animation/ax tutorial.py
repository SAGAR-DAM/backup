# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 10:01:58 2023

@author: sagar
"""
import numpy as np
import matplotlib.pyplot as plt

l=[1,2]
x,y,=l
print(x)
print(y)

# Animation setup
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-3.5, 3.5), ylim=(-3.5, 6.5))
ax.set_aspect('equal')
ax.grid()

lineprime, =ax.plot([],[],'ko-', lw=2,markersize=15)
line, = ax.plot([], [], 'ro-', lw=2, markersize=15)
line1, = ax.plot([], [], 'r--', lw=0.5)
line2, = ax.plot([], [], 'k--', lw=1)
centre, =ax.plot([],[],'bo', markersize=15)

line1
#line1.set_data([0,1],[0,6])
#line1