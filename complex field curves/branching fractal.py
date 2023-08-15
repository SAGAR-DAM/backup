# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 14:33:25 2023

@author: sagar
"""

from turtle import *

#function to create koch branching_fractal
def branching_fractal(lengthSide, levels):
    if levels == 0:
        forward(lengthSide)
        return
    else:
        lengthSide /= 3.0
        branching_fractal(lengthSide, levels-1)
        left(90)
        branching_fractal(lengthSide, levels-1)
        right(90)
        branching_fractal(lengthSide, levels-1)
        right(90)
        branching_fractal(lengthSide, levels-1)
        left(90)
        branching_fractal(lengthSide, levels-1)
        
# main function
if __name__ == "__main__":

    #defining the speed of the turtle
    speed(1000)				
    length = 600.0			

    # Pull the pen up – no drawing when moving.
    penup()					
    
    # Move the turtle backward by distance,
    # opposite to the direction the turtle
    # is headed.
    # Do not change the turtle’s heading.
    backward(length/2.0)		
    # Pull the pen down – drawing when moving.
    pendown()		
    
    
    level=4
    
    branching_fractal(length,level)
    right(180)
    branching_fractal(length,level)

    # To control the closing windows of the turtle
    mainloop()