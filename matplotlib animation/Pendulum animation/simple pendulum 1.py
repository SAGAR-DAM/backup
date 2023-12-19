# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 12:57:44 2023

@author: sagar
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#import matplotlib
#matplotlib.rcParams['figure.dpi']=300 # highres display

g=981
sim_time=10
dt=0.005

class pendulum:
    def __init__(self,m,L,theta,theta_dot):#,theta_dot,theta_ddot):
        self.m=m
        self.L=L
        self.theta=theta
        self.theta_dot=theta_dot
        
    def propagator(self,state):
        global g
        global dt
        self.theta,self.theta_dot=state
        theta_ddot=-(g/self.L)*np.sin(self.theta)
        
        self.theta_dot+=theta_ddot*dt
        self.theta+=(self.theta_dot*dt)#+theta_ddot*dt**2/2)
        current_info=[self.theta,self.theta_dot]
        return(current_info)

p1=pendulum(10,2,np.pi/6,0.1)
p2=pendulum(8,6,-np.pi,0.0001)
p3=pendulum(20,5,-np.pi/4,0)

p=[p1,p2,p3]  #give the pendulums on which you want simulation

no_of_pendulum=len(p)

t=np.arange(0,sim_time,dt)
states=np.empty((no_of_pendulum,len(t),2))
for i in range(no_of_pendulum):
    states[i][0]=[p[i].theta,p[i].theta_dot]

for i in range(no_of_pendulum):
    for j in range(1,len(t)):
        states[i][j]=p[i].propagator(states[i][j-1])
    
# Animation setup
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=True, xlim=(-9, 9), ylim=(-9, 9))
ax.set_aspect('equal')
ax.grid(True)
ax.axis(True)
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
line1, = ax.plot([], [], 'ro-', lw=0.5, markersize=10)
line2, = ax.plot([], [], 'bo-', lw=0.5, markersize=10)
line3, = ax.plot([], [], 'ko-', lw=0.5, markersize=10)

line=[line1,line2,line3]


def init():
    global line
    for j in range(len(line)):
        line[i].set_data([], [])
    return line

def animate(i):
    global p
    for j in range(no_of_pendulum):
        x=[0,p[j].L*np.sin(states[j][i,0])]
        y=[0,-p[j].L*np.cos(states[j][i,0])]
        line[j].set_data(x,y)
    return line

ani = animation.FuncAnimation(fig, animate, range(1, len(states[0])),
                              interval=dt*50, init_func=init, repeat=True)
plt.show()

for __var__ in dir():
    exec('del '+ __var__)
    del __var__