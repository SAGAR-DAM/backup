# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 15:25:55 2023

@author: sagar
"""



from turtle import *

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

	# Pull the pen down – drawing when moving.
	pendown()		

	snowflake(length,5)

	# To control the closing windows of the turtle
	mainloop()
