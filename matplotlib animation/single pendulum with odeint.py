# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 09:11:11 2023

@author: sagar
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def derivatives(states,t):
    k=5
    theta,z=states
    dtheta_dt=z
    dz_dt=-k**2*np.sin(theta)
    d_states=np.array([dtheta_dt,dz_dt])
    return d_states

t=np.linspace(0,10,1001)
sol=odeint(derivatives,(np.pi/2,0),t)

sol=sol.T

plt.plot(t,sol[0],'k-')
plt.plot(t,sol[1],'r--')
plt.show()


import sys
import pygame
from PIL import Image
# Screen settings
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Double Pendulum Animation")
pivot = (width // 2, 300)
clock = pygame.time.Clock()
frames=[]


i=0
running = True
savegif=False      # True if you want to save the gif. False if not.
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
''' Main Loop '''

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Clear the screen
    screen.fill(black)
    if i<len(sol[0]):
        pend_x=pivot[0] + 200* np.sin(sol[0][i])
        pend_y=pivot[0] + 200* np.cos(sol[0][i])
        pygame.draw.line(screen, colors[0], pivot, (pend_x, pend_y), 1)
        pygame.draw.circle(screen, colors[1], (int(pend_x), int(pend_y)), 10)
        
        if (savegif==True):
            pygame_image = pygame.surfarray.array3d(screen)
            pil_image = Image.fromarray(pygame_image)
            pil_image = pil_image.rotate(-90, expand=True)
            
            # Append the frame to the list
            frames.append(pil_image)
    else:
        running=False
    i+=1
    pygame.display.flip()
    clock.tick(150)
    
if(savegif==True):
    # Save the list of frames as a GIF
    frames[0].save("D:\\Codes\\matplotlib animation\\dragged_pendulum_animation.gif", save_all=True, append_images=frames[1:], loop=0, duration=20)
    
pygame.quit()
sys.exit()

for __var__ in dir():
    exec('del '+ __var__)
    del __var__