# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 15:49:25 2023

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
t=0

# Screen settings
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Double Pendulum Animation")

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

class inverted_pendulum:
    def __init__(self,m,L,theta,theta_dot,A,omega,pivot):
        self.m=m
        self.L=L
        self.theta=theta
        self.theta_dot=theta_dot
        self.A=A
        self.omega=omega
        self.pivot=pivot
        
##########################################################################################
##########################################################################################
'''  Input Parameters '''
##########################################################################################
##########################################################################################

p1=inverted_pendulum(m=40, L=200, theta=np.pi/12, theta_dot=-0.1, A=20, omega=15,pivot = (width // 2, 300))
p2=inverted_pendulum(m=40, L=200, theta=np.pi/12, theta_dot=-0.1, A=5, omega=15,pivot = (width // 2+100, 300))
p=[p1]#,p2]

savegif=False

##########################################################################################
##########################################################################################
'''  All Required helping variables 

             with Main loop
'''
##########################################################################################
##########################################################################################


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
        m=p[i].m
        L=p[i].L
        theta=p[i].theta
        theta_dot=p[i].theta_dot
        A=p[i].A
        omega=p[i].omega
        pivot=p[i].pivot
        t=t+dt
        
        theta_ddot=np.sin(theta)*(g-A*omega**2*np.cos(omega*t))/L
        theta_dot+=theta_ddot*dt
        theta+=theta_dot*dt
        
        p[i].theta=theta
        p[i].theta_dot=theta_dot
        
        # Draw the pendulums
        base_x=pivot[0]
        base_y=pivot[1]+A*np.cos(omega*t)
        
        pendulum_x=base_x+L*np.sin(theta)
        pendulum_y=base_y-L*np.cos(theta)
        
        pygame.draw.line(screen, colors[0], (base_x,base_y), (pendulum_x, pendulum_y), 1)
        pygame.draw.circle(screen, colors[1], (pendulum_x,pendulum_y), 10)
        pygame.draw.rect(screen, colors[2],(base_x-10,base_y-10,20,20))
    
    
    
    
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
    frames[0].save("D:\\Codes\\matplotlib animation\\inverted_pendulum_animation.gif", save_all=True, append_images=frames[1:], loop=0, duration=50)

pygame.quit()
sys.exit()