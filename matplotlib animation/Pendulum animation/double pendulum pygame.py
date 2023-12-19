
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 17:32:05 2023

@author: sagar
"""
import numpy as np
import sys
import pygame
from PIL import Image


##########################################################################################
##########################################################################################
'''  All Required parameters and defined objects (Double pendulum '''
##########################################################################################
##########################################################################################

g=200
dt=0.035

# Screen settings
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Double Pendulum Animation")
pivot = (width // 2, 300)

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green =(0,255,0)
blue=(0,0,255)
red1=(120,0,0)
green1=(0,120,0)
blue1=(0,0,120)
yellow=(255,255,0)
magenta=(255,0,255)
cyan=(0,255,255)

colors=[white,red,green,blue,red1,green1,blue1,yellow,magenta,cyan]
len_c=len(colors)

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


##########################################################################################
##########################################################################################
'''  Input Parameters '''
##########################################################################################
##########################################################################################

p1=double_pendulum(m1=40, m2=10, L1=120, L2=150, theta1=np.pi, theta2=np.pi, theta1_dot=0.01, theta2_dot=0.01)
p2=double_pendulum(m1=40, m2=10, L1=120, L2=150, theta1=np.pi, theta2=np.pi, theta1_dot=0.011, theta2_dot=0.01)
p3=double_pendulum(m1=10, m2=20, L1=100, L2=160, theta1=np.pi/6, theta2=np.pi, theta1_dot=0.0, theta2_dot=0)

p=[p1,p2]#,p3]       # add the pendulums you want the animation for
savegif=False      # True if you want to save the gif. False if not.


##########################################################################################
##########################################################################################
'''  All Required helping variables 

             with Main loop
'''
##########################################################################################
##########################################################################################


no_of_pendulum=len(p)
clock = pygame.time.Clock()
frames=[]

running = True

''' Main Loop '''

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Clear the screen
    screen.fill(black)
    
    for i in range(len(p)):
        m1=p[i].m1
        m2=p[i].m2
        L1=p[i].L1
        L2=p[i].L2
        theta1=p[i].theta1
        theta2=p[i].theta2
        theta1_dot=p[i].theta1_dot
        theta2_dot=p[i].theta2_dot
        
        delta_theta=theta1-theta2
        
        theta1_ddot=(-m2*L1*theta1_dot**2*np.sin(delta_theta)*np.cos(delta_theta)\
                     -m2*L2*theta2_dot**2*np.sin(delta_theta)\
                         +m2*g*np.sin(theta2)*np.cos(delta_theta)\
                             -(m1+m2)*g*np.sin(theta1))\
            /((m1+m2)*L1-m2*L1*(np.cos(delta_theta))**2)
            
        theta2_ddot=-(m2*L1*np.cos(delta_theta)*theta1_ddot\
                      -m2*L1*theta1_dot**2*np.sin(delta_theta)\
                          +m2*g*np.sin(theta2))\
            /(m2*L2)
            
        theta1_dot+=theta1_ddot*dt
        theta2_dot+=theta2_ddot*dt
        
        theta1+=(theta1_dot*dt)#+theta1_ddot*dt**2/2)
        theta2+=(theta2_dot*dt)#+theta2_ddot*dt**2/2)
        
        p[i].theta1=theta1
        p[i].theta2=theta2
        
        p[i].theta1_dot=theta1_dot
        p[i].theta2_dot=theta2_dot

        # Draw the pendulums
        pendulum1_x = pivot[0] + L1* np.sin(theta1)
        pendulum1_y = pivot[1] + L1* np.cos(theta1)
        pendulum2_x = pendulum1_x + L2 * np.sin(theta2)
        pendulum2_y = pendulum1_y + L2 * np.cos(theta2)
    
        pygame.draw.line(screen, colors[i], pivot, (pendulum1_x, pendulum1_y), 1)
        pygame.draw.line(screen, colors[i], (pendulum1_x, pendulum1_y), (pendulum2_x, pendulum2_y), 1)
        pygame.draw.circle(screen, colors[-i-1], (int(pendulum1_x), int(pendulum1_y)), 10)
        pygame.draw.circle(screen, colors[-i-1], (int(pendulum2_x), int(pendulum2_y)), 10)
        
    if (savegif==True):
        pygame_image = pygame.surfarray.array3d(screen)
        pil_image = Image.fromarray(pygame_image)
        pil_image = pil_image.rotate(-90, expand=True)
        
        # Append the frame to the list
        frames.append(pil_image)
    
    pygame.display.flip()
    clock.tick(60)

if(savegif==True):
    # Save the list of frames as a GIF
    frames[0].save("D:\\Codes\\matplotlib animation\\double_pendulum_animation.gif", save_all=True, append_images=frames[1:], loop=0, duration=50)


pygame.quit()
sys.exit()

for __var__ in dir():
    exec('del '+ __var__)
    del __var__