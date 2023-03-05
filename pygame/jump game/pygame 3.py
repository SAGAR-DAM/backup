# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 13:25:28 2022

@author: mrsag
"""
##############################################
#Imports 
import numpy as np
import pygame
import sys
import time
from pygame.locals import *
import random
##############################################

def main():

    pygame.init()  # initiates pygame


    clock=pygame.time.Clock() #clock

    #player 

    #player 0
    ##################################################################################
    player_image=pygame.image.load("D:\python files\player_02.png")
    player_scale=15
    player_image=pygame.transform.scale(player_image,(player_image.get_width()/player_scale,player_image.get_height()/player_scale))
    player_location=[50,50] #player location initially
    x=player_location[0]  #player x coordinate
    y=player_location[1]  #player y coordinate
    player_y_momentum=0
    player_rect=pygame.Rect(50,50,player_image.get_width(),player_image.get_height()) #will be used to determine the collision with the player with other object
    test_rect=pygame.Rect(80,100,100,50)  #test rect for collision check
    player_direction='none'
    keypressnumber=0


    #playing window
    ##################################################################################
    window=500
    window_size=[window*1.5,window]  #window size
    screen=pygame.display.set_mode(window_size,0,32)  
    display=pygame.Surface((window_size[0],window_size[1]))
    pygame.display.set_caption("SAGAR Game window")  #window name

    player_image.set_colorkey((0,150,255))
    ##################################################################################


    #other display
    ##################################################################################
    grass=pygame.image.load("D:\python files\grass.png")
    dirt=pygame.image.load("D:\python files\soil1.png")
    cloud=pygame.image.load("D:\python files\cloud.png")
    diamond=pygame.image.load("D:\python files\diamond.jpg")
    sun=pygame.image.load("D:\python files\sun.png")
    tile_size=10            #game map structure parameter
    grass=pygame.transform.scale(grass,(tile_size,tile_size))
    dirt=pygame.transform.scale(dirt,(tile_size,tile_size))
    cloud=pygame.transform.scale(cloud,(75,75))
    sun=pygame.transform.scale(sun,(100,75))
    diamond=pygame.transform.scale(diamond,(20,20))
    diamondnumber=10

    diax=[]
    diay=[]
    for i in range(diamondnumber):
        diax.append(random.randint(0,window_size[0]))
        diay.append(random.randint(0,window_size[1]))
        
    # Game map:
    ##################################################################################
    row=int(window_size[1]/tile_size)
    column=int(window_size[0]/tile_size)

    game_map=np.matrix([[0]*column]*row,dtype=str)

    for i in range(row):
        for j in range(column):      #numbers in if condition will depend on the parameter tile_size
            if i<40:
                game_map[i,j]='0'
            elif (i==40):
                if (15<=j<=60):
                    game_map[i,j]='0'
                else:
                    game_map[i,j]='1'
            elif(i==41):
                if (15<=j<=60):
                    game_map[i,j]='0'
                else:
                    game_map[i,j]='2'
            else:
                game_map[i,j]='2'
    for i in range(20,21,1):   #numbers will depend on the parameter tile_size
        for j in range(15,60,1):
            game_map[i+3*int(j/15),j]='1'
            game_map[i+1+3*int(j/15),j]='2'
            

    # test purpose game map (in generally should be in comment)

    #for i in range(row):
    #    for j in range(column):
    #        if i>=row-10:
    #            game_map[i,j]=2
            
    ##################################################################################



    def collision_test(rect,tiles):
        hit_list=[]
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def move(rect,movement,tiles):
        collision_types={'top':False,'bottom':False,'right':False,'left':False}
        rect.x+=movement[0]
        hit_list=collision_test(rect,tiles)
        for tile in hit_list:
            if movement[0]>0:
                rect.right=tile.left
                collision_types['right']=True
            elif movement[0]<0:
                rect.left=tile.right
                collision_types['left']=True
        rect.y+=movement[1]
        hit_list=collision_test(rect,tiles)
        for tile in hit_list:
            if movement[1]>0:
                rect.bottom=tile.top
                collision_types['bottom']=True
            elif movement[1]<0:
                rect.top=tile.bottom
                collision_types['top']=True
        
        return rect,collision_types
        
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
        display.fill((0,150,255))  #fill the screen with a colour at new frame
        
        #filling the display with other stuffs
        tile_rects=[]
        xd=0
        for i in range(int(window_size[1]/tile_size)):
            yd=0
            for j in range(int(window_size[0]/tile_size)):
                if game_map[i,j]=='1':
                    display.blit(grass,(yd,xd))
                elif game_map[i,j]=='2':
                    display.blit(dirt,(yd,xd))
                
                if game_map[i,j]!='0':
                    tile_rects.append(pygame.Rect(yd,xd,tile_size,tile_size)) 
                    #pygame.draw.rect(display,(0,0,0),pygame.Rect(yd,xd,tile_size,tile_size))
                yd+=tile_size
            xd+=tile_size
        
        #for i in range(len(tile_rects)):
        #   pygame.draw.rect(display,(0,0,0),tile_rects[i])
        
        display.blit(sun,((window_size[0]/2+window_size[0]/2+150)/2-15,(window_size[1]*1/4-50+window_size[1]*1/4-100)/2))
        display.blit(cloud,(window_size[0]/2,window_size[1]*1/4-50))
        display.blit(cloud,(window_size[0]/2+150,window_size[1]*1/4-100))
        
        
        for i in range(diamondnumber):
            display.blit(diamond,(diax[i],diay[i]))   
            
        '''commented in 2-3'''
        #Player position and momentum
        #display.blit(player_image,(x,y))   #moving the player at new screen
        
        #if (player_location[1]> window_size[1]-player_image.get_height()-110):  
        #    player_y_momentum=-player_y_momentum   #keeping the palyer in screen
        #else:
        #    player_y_momentum+=0.2  #increasing the free fall speed of the player
        #player_y_momentum+=0.2
        #player_location[1]+=player_y_momentum  #player falling under gravity
        
        #player_rect.x=x #moving the player rect with the player
        #player_rect.y=y #  "    "    "     "
        #####################################################################
        
        
        #check collision with player and test rect
        #####################################################################
        if player_rect.colliderect(test_rect):  #Collision test with the test rect
            pygame.draw.rect(display,(0,255,0),test_rect)
        else:
            pygame.draw.rect(display,(255,255,255),test_rect)
        #####################################################################
        
        '''commented in 2-3'''
        #Player movement module
        #####################################################################
        #if moving_right==True:  #player move right
        #    player_location[0] += 4
        #if moving_left==True:   #player move left
        #    player_location[0] -=4
        #if moving_up==True:   #player move up
        #    player_location[1] -=4
        #if moving_down==True:   #player move left
        #    player_location[1] +=4 
        #####################################################################
        
        
        player_movement=[0,0]
        if moving_right==True:
            player_movement[0] +=4
            player_direction='right'
        if moving_left==True:
            player_movement[0] -=4
            player_direction='left'
        
            
        player_movement[1] +=player_y_momentum
        player_y_momentum +=0.3
        
        if player_y_momentum>10:
            player_y_momentum=10
        
        if moving_up==True and collisions['bottom']==True:
            player_y_momentum=-8    
            
        player_rect, collisions = move(player_rect,player_movement,tile_rects)
        if collisions['top']==True:
            player_y_momentum=-player_y_momentum
            
            
        display.blit(player_image,(player_rect.x,player_rect.y))
        
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
                    if player_direction=='left':
                        player_image=pygame.transform.flip(player_image,True,False)#flipping player
                    
                if event.key==K_LEFT:   #move left activation
                    moving_left=True
                    if player_direction=='right':
                        player_image=pygame.transform.flip(player_image,True,False)#flipping player
                
                if event.key==K_UP:   #move up activation
                    if collisions['bottom']==True:
                        player_y_momentum=-10
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
        surf=pygame.transform.scale(display,window_size)
        screen.blit(surf,(0,0))
        pygame.display.update()    #screen update
        clock.tick(60)  #frames per second







if __name__=='__main__':
    main()