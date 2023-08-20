# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 21:37:49 2023

@author: sagar
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 15:25:55 2023

@author: sagar
"""

from turtle import *
import numpy as np

#function to create koch snowflake or koch curve
def snowflake(lengthSide, levels):
    if levels == 0:
        forward(lengthSide)
        return
    else:
        lengthSide /= 3.0
        snowflake(lengthSide, levels-1)
        left(60)
        snowflake(lengthSide, levels-1)
        right(120)
        snowflake(lengthSide, levels-1)
        left(60)
        snowflake(lengthSide, levels-1)
        
# main function
if __name__ == "__main__":

    # defining the speed of the turtle
    speed(1000)				
    length = 600.0			

    # Pull the pen up – no drawing when moving.
    penup()					
    
    # Move the turtle backward by distance,
    # opposite to the direction the turtle
    # is headed.
    # Do not change the turtle’s heading.
    backward(length/2.0)		
    left(90)
    forward(200)
    right(90)

    # Pull the pen down – drawing when moving.
    pendown()		

    level=3
    
    for i in range(6):
        
        snowflake(length,level)
        right(120)
        snowflake(length,level)
        right(120)
        snowflake(length,level)
    
    
        right(120)
        penup()
        l=length/6
        forward(l)
        right(90)
        forward(l*np.tan(np.pi/6))
        left(90)
        pendown()
    
        length-=2*l
    
    
    hideturtle()
    # To control the closing windows of the turtle
    mainloop()
