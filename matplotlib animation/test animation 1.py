# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 11:01:00 2023

@author: sagar
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
G =  5.81  # acceleration due to gravity (m/s^2)
L1 = 1.0  # length of the first pendulum (m)
L2 = 2.0  # length of the second pendulum (m)
M1 = 2.0  # mass of the first pendulum (kg)
M2 = 6.0  # mass of the second pendulum (kg)

# Initial conditions
theta1 = np.pi / 1  # initial angle of the first pendulum (rad)
theta2 = 3*np.pi / 4  # initial angle of the second pendulum (rad)
omega1 = 0.0  # initial angular velocity of the first pendulum (rad/s)
omega2 = 1.0  # initial angular velocity of the second pendulum (rad/s)

# Time parameters
dt = 0.0025  # time step (s)
t = np.arange(0, 18, dt)

# Function to compute derivatives of state variables
def derivatives(state, t):
    theta1, omega1, theta2, omega2 = state

    theta1_dot = omega1
    omega1_dot = (-G * (2 * M1 + M2) * np.sin(theta1) - M2 * G * np.sin(theta1 - 2 * theta2) - 2 * np.sin(theta1 - theta2) * M2 * (omega2**2 * L2 + omega1**2 * L1 * np.cos(theta1 - theta2))) / (L1 * (2 * M1 + M2 - M2 * np.cos(2 * theta1 - 2 * theta2)))

    theta2_dot = omega2
    omega2_dot = (2 * np.sin(theta1 - theta2) * (omega1**2 * L1 * (M1 + M2) + G * (M1 + M2) * np.cos(theta1) + omega2**2 * L2 * M2 * np.cos(theta1 - theta2))) / (L2 * (2 * M1 + M2 - M2 * np.cos(2 * theta1 - 2 * theta2)))

    return np.array([theta1_dot, omega1_dot, theta2_dot, omega2_dot])

# Simulate the double pendulum motion
states = np.empty((len(t), 4))
states[0] = [theta1, omega1, theta2, omega2]

tracex1=[]
tracey1=[]

tracex2=[]
tracey2=[]

centre=[]

for i in range(1, len(t)):
    states[i] = states[i - 1] + derivatives(states[i - 1], t[i - 1]) * dt

# Animation setup
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-3.5, 3.5), ylim=(-3.5, 3.5))
ax.set_aspect('equal')
ax.grid()

lineprime, =ax.plot([],[],'ko-', lw=2,markersize=15)
line, = ax.plot([], [], 'ro-', lw=2, markersize=15)
line1, = ax.plot([], [], 'r--', lw=0.5)
line2, = ax.plot([], [], 'k--', lw=1)
centre, =ax.plot([],[],'bo', markersize=15)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    lineprime.set_data([],[])
    line.set_data([], [])
    line1.set_data([],[])
    line2.set_data([],[])
    centre.set_data([],[])
    time_text.set_text('')
    return line, time_text

def animate(i):
    global ax
    thisx = [0, L1 * np.sin(states[i, 0]), L1 * np.sin(states[i, 0]) + L2 * np.sin(states[i, 2])]
    thisy = [0, -L1 * np.cos(states[i, 0]), -L1 * np.cos(states[i, 0]) - L2 * np.cos(states[i, 2])]
    tracex1.append(thisx[1])
    tracey1.append(thisy[1])
    tracex2.append(thisx[2])
    tracey2.append(thisy[2])
    
    lineprime.set_data(thisx[1:],thisy[1:])
    line.set_data(thisx[:2], thisy[:2])
    line1.set_data(tracex1,tracey1)
    line2.set_data(tracex2,tracey2)
    centre.set_data([0],[0])
    time_text.set_text(time_template % (i*dt))
    return lineprime,line, line1, line2, centre, time_text

ani = animation.FuncAnimation(fig, animate, range(1, len(states)),
                              interval=dt*50, blit=True, init_func=init, repeat=False)
plt.show()
