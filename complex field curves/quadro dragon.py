# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 15:25:55 2023

@author: sagar
"""



from turtle import *
import numpy as np
#function to create koch snowflake or koch curve
def dragon(L,level,prime):
        if(prime==0):
            if(level==0):
                forward(L/np.sqrt(2))
                right(90)
                forward(L/np.sqrt(2))
            else:
                L/=np.sqrt(2)
                dragon(L,level-1,0)
                right(90)
                dragon(L,level-1,1)
        elif(prime==1):
            if(level==0):
                forward(L/np.sqrt(2))
                left(90)
                forward(L/np.sqrt(2))
            else:
                L/=np.sqrt(2)
                dragon(L,level-1,0)
                left(90)
                dragon(L,level-1,1)
        
# main function
if __name__ == "__main__":

    # defining the speed of the turtle
    speed(1000)				
    length = 300.0			

    # Pull the pen up – no drawing when moving.
    penup()					
    
    # Move the turtle backward by distance,
    # opposite to the direction the turtle
    # is headed.
    # Do not change the turtle’s heading.
    backward(length/2.0)		
    left(90)
    forward(50)
    right(90)

    # Pull the pen down – drawing when moving.
    pendown()		

    level=10
    
    dragon(length,level,0)
    penup()
    right(135+level*45)
    forward(length)
    right(135-level*45)
    left(90)
    pendown()
    
    pencolor("red")
    dragon(length,level,0)
    penup()
    right(135+level*45)
    forward(length)
    right(135-level*45)
    left(90)
    pendown()
    
    
    pencolor("green")
    dragon(length,level,0)
    penup()
    right(135+level*45)
    forward(length)
    right(135-level*45)
    left(90)
    pendown()
    
    pencolor("blue")
    dragon(length,level,0)
    
    hideturtle()
    # To control the closing windows of the turtle
    mainloop()