# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 22:37:24 2023

@author: sagar
"""

# Draw a Koch snowflake
# Python program to print partial Koch Curve.
# importing the libraries : turtle standard
# graphics library for python
from turtle import *

#function to create koch snowflake or koch curve
def snowflake(lengthSide, levels):
	if levels == 0:
		forward(lengthSide)
		return
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

	snowflake(length,2)

	# To control the closing windows of the turtle
	mainloop()
