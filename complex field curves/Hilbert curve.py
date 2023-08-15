# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 15:25:55 2023

@author: sagar
"""

from turtle import *

def Hilbert(L,level,prime):
    if(prime==0):
        if (level==0):
            forward(L/3)
            right(90)
            forward(L/3)
            right(90)
            forward(L/3)
            
        elif(level%2==1):
            L /= 2
            l=L/10
            Hilbert(L,level-1,1)
            right(90)
            forward(l)
            Hilbert(L,level-1,0)
            left(90)
            forward(l)
            left(90)
            Hilbert(L,level-1,0)
            forward(l)
            right(90)
            Hilbert(L,level-1,1)
            
        elif(level%2==0):
            L /=2
            l=L/10
            Hilbert(L,level-1,1)
            forward(l)
            right(90)
            Hilbert(L,level-1,0)
            forward(l)
            Hilbert(L,level-1,0)
            right(90)
            forward(l)
            Hilbert(L,level-1,1)
            
            
    elif(prime==1):
        if(level==0):
            forward(L/3)
            left(90)
            forward(L/3)
            left(90)
            forward(L/3)
            
        elif(level%2==1):
            L /=2
            l=L/10
            Hilbert(L,level-1,0)
            left(90)
            forward(l)
            Hilbert(L,level-1,1)
            right(90)
            forward(l)
            right(90)
            Hilbert(L,level-1,1)
            forward(l)
            left(90)
            Hilbert(L,level-1,0)
            
        elif(level%2==0):
            L /=2
            l=L/10
            Hilbert(L,level-1,0)
            forward(l)
            left(90)
            Hilbert(L,level-1,1)
            forward(l)
            Hilbert(L,level-1,1)
            left(90)
            forward(l)
            Hilbert(L,level-1,0)
    






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
    # Pull the pen down – drawing when moving.
    pendown()		

    Hilbert(length,5,0)

    # To control the closing windows of the turtle
    mainloop()