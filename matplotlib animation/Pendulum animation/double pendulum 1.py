# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 10:19:41 2023

@author: sagar
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

g=980
sim_time=10
dt=0.005

class double_pendulum:
    def __init__(self,m1,m2,L1,L2,theta1,theta2,theta1_dot,theta2_dot):
        self.m1=m1
        self.m2=m2
        self.L1=L1
        self.L2=L2
        self.theta1=theta1
        self.theta2=theta2
        self.theta1_dot=theta1_dot
        self.theta2_dot=theta2_dot
        
    def propagator(self,state):
        global g
        global dt
        self.theta1,self.theta2,self.theta1_dot,self.theta2_dot=state
        
        delta_theta=self.theta1-self.theta2
        theta1_ddot=(-self.m2*self.L1*self.theta1_dot**2*np.sin(delta_theta)*np.cos(delta_theta)\
                     -self.m2*self.L2*self.theta2_dot**2*np.sin(delta_theta)\
                         +self.m2*g*np.sin(self.theta2)*np.cos(delta_theta)\
                             -(self.m1+self.m2)*g*np.sin(self.theta1))\
            /((self.m1+self.m2)*self.L1-self.m2*self.L1*(np.cos(delta_theta))**2)
            
        theta2_ddot=-(self.m2*self.L1*np.cos(delta_theta)*theta1_ddot\
                      -self.m2*self.L1*self.theta1_dot**2*np.sin(delta_theta)\
                          +self.m2*g*np.sin(self.theta2))\
            /(self.m2*self.L2)
            
        self.theta1_dot+=theta1_ddot*dt
        self.theta2_dot+=theta2_ddot*dt
        
        self.theta1+=(self.theta1_dot*dt)#+theta1_ddot*dt**2/2)
        self.theta2+=(self.theta2_dot*dt)#+theta2_ddot*dt**2/2)
        
        current_info=[self.theta1,self.theta2,self.theta1_dot,self.theta2_dot]
        
        return(current_info)
    
p1=double_pendulum(m1=10, m2=4, L1=4, L2=5, theta1=np.pi, theta2=np.pi, theta1_dot=-0.001, theta2_dot=0.2)
p2=double_pendulum(m1=10, m2=4, L1=4, L2=5, theta1=np.pi, theta2=np.pi, theta1_dot=-0.01, theta2_dot=0.01)

p=[p1]

no_of_pendulum=len(p)

t=np.arange(0,sim_time,dt)
states=np.empty((no_of_pendulum,len(t),4))
#traces=np.empty((no_of_pendulum,len(t),2))

for i in range(no_of_pendulum):
    states[i][0]=[p[i].theta1,p[i].theta2,p[i].theta1_dot,p[i].theta2_dot]

for i in range(no_of_pendulum):
    for j in range(1,len(t)):
        states[i][j]=p1.propagator(states[i][j-1])
    
# Animation setup
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=True, xlim=(-9, 9), ylim=(-9, 9))
ax.set_aspect('equal')
ax.grid(True)
ax.axis(True)
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
line1, = ax.plot([], [], 'ro-', lw=0.5, markersize=10)
trace1, =ax.plot([], [], '--', lw=0.5)
#line2, = ax.plot([], [], 'bo-', lw=0.5, markersize=10)
#trace2, =ax.plot([], [], '--', lw=0.5)
#line3, = ax.plot([], [], 'ko-', lw=0.5, markersize=10)
#trace3, =ax.plot([], [], '--', lw=0.5)

line=[line1]#,line2]#,line3]
trace=[trace1]#,trace2]#,trace3]

tracex=[]
tracey=[]

def init():
    global line
    for j in range(len(line)):
        line[i].set_data([], [])
        trace[i].set_data([], [])
    return line,trace

def animate(i):
    global p
    for j in range(no_of_pendulum):
        x=[0,p[j].L1*np.sin(states[j][i,0]),p[j].L1*np.sin(states[j][i,0])+p[j].L2 *np.sin(states[j][i, 1])]
        y=[0,-p[j].L1*np.cos(states[j][i,0]),-p[j].L1*np.cos(states[j][i, 0])-p[j].L2*np.cos(states[j][i, 1])]
        
        tracex.append(x[2])
        tracey.append(y[2])
        
        line[j].set_data(x,y)
        trace[j].set_data(tracex,tracey)
    return line,trace

ani = animation.FuncAnimation(fig, animate, range(1, len(states[0])),
                              interval=dt*50, init_func=init, repeat=True)
plt.show()
#ani.save("D:\\Codes\\matplotlib animation\\double pendulum.gif",fps=150, writer= "pillow", dpi=300)