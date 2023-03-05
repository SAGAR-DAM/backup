# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 13:25:28 2022

@author: mrsag
"""
##############################################
#Imports 

import pygame
import sys
import time
from pygame.locals import *
##############################################

pygame.init()  # initiates pygame


clock=pygame.time.Clock() #clock

#player 
##################################################################################
player_image=pygame.image.load("D:\python files\duck.png") #player image upload
player_image=pygame.transform.scale(player_image,(50,50))  #player size
player_location=[50,50] #player location initially
x=player_location[0]  #player x coordinate
y=player_location[1]  #player y coordinate
player_y_momentum=0
player_rect=pygame.Rect(x,y,player_image.get_width(),player_image.get_height()) #will be used to determine the collision with the player with other object
test_rect=pygame.Rect(80,100,100,50)  #test rect for collision check
##################################################################################


#playing window
##################################################################################
window=500
window_size=[window,window]  #window size
screen=pygame.display.set_mode(window_size,0,32)  
pygame.display.set_caption("Game window")  #window name
##################################################################################

#movement
##################################################################################
moving_right=False
moving_left=False
moving_up=False
moving_down=False
##################################################################################


#MAIN game loop
##################################################################################
##################################################################################
##################################################################################

while True: # game loop

    #player location update
    #####################################################################
    x=player_location[0]  #player x coordinate
    y=player_location[1]  #player y coordinate
    screen.fill((200,0,0))  #fill the screen with a colour at new frame
    screen.blit(player_image,(x,y))   #moving the player at new screen
    
    if (player_location[1]> window_size[1]-player_image.get_height()):  
        player_y_momentum=-player_y_momentum   #keeping the palyer in screen
    else:
        player_y_momentum+=0.2  #increasing the free fall speed of the player
    player_location[1]+=player_y_momentum  #player falling under gravity
    
    player_rect.x=x #moving the player rect with the player
    player_rect.y=y #  "    "    "     "
    #####################################################################
    
    
    #check collision with player and test rect
    #####################################################################
    if player_rect.colliderect(test_rect):  #Collision test with the test rect
        pygame.draw.rect(screen,(0,255,0),test_rect)
    else:
        pygame.draw.rect(screen,(255,255,255),test_rect)
    #####################################################################
    
    
    #Player movement module
    #####################################################################
    if moving_right==True:  #player move right
        player_location[0] += 4
    if moving_left==True:   #player move left
        player_location[0] -=4
    if moving_up==True:   #player move up
        player_location[1] -=4
    if moving_down==True:   #player move left
        player_location[1] +=4 
    #####################################################################
    
    
    #Checking different inputs from keyboard
    #####################################################################
     
    for event in pygame.event.get():
        
        if event.type==QUIT:#closing the screen
            pygame.quit()
            sys.exit()
        
        #Check for movement activation
        if event.type==KEYDOWN:  #activating the arrow keys
            if event.key==K_RIGHT:  #move right activation
                moving_right=True
            if event.key==K_LEFT:   #move left activation
                moving_left=True
            if event.key==K_UP:   #move up activation
                moving_up=True
            if event.key==K_DOWN:   #move down activation
                moving_down=True
                
        #check for the movement deactivation       
        if event.type==KEYUP:
            if event.key==K_RIGHT:   #move right deactivation
                moving_right=False
            if event.key==K_LEFT:   #move left deactivation
                moving_left=False
            if event.key==K_UP:   #move up deactivation
                moving_up=False
            if event.key==K_DOWN:   #move down deactivation
                moving_down=False
                
    x=player_location[0]  #player x coordinate
    y=player_location[1]  #player y coordinate
    pygame.display.update()    #screen update
    clock.tick(60)  #frames per second
