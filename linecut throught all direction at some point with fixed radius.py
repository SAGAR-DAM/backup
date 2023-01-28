# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 23:53:08 2023

@author: Sagar Dam
"""
# A CODE FOR GENERAL LINECUT THROUGH SOME POINT AND TOWARDS ALL DIRECTIONS.
''' 
This is a code to get the linecuts through some point of any image. The point pixel index should be given and 
the lines are in some 10 degree interval. By changing the linecut degree intervals, we can take any number of 
linecuts through the given point. 
'''

import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from PIL import Image, ImageDraw

# Load the image
image_path='D:\\data Lab\\frog\\Granouille allignment\\16jan2023\\ids raw\\5_33.png'
image = io.imread(image_path)
image2 = Image.open(image_path)

#####################################################################################

point=[288,384]    #The point for which the linecut is needed.

#radius=50
x=point[0]         #x coordinate (row of the matrix)
y=point[1]         #y coordinate (column of the matrix)

X=image.shape[0]-1
Y=image.shape[1]-1

boundary_distances=[x,y,X-x,Y-y]    # distances of boundary from the given point

radius=min(boundary_distances)

#####################################################################################
theta_degree=np.linspace(0,170,18)
theta=theta_degree*np.pi/180
####################################################################################

def draw_on_image(image,x,y):
    draw = ImageDraw.Draw(image)
    draw.line((x[1],x[0],y[1],y[0]), fill=(255, 0, 0), width=2)
    return(image)
    
def linecut_function(start_point,end_point,image,image2):
    # Use the numpy function linspace to get the coordinates of the line
    num=round(np.sqrt((start_point[0]-end_point[0])**2+(start_point[1]-end_point[1])**2))
    x, y = np.linspace(start_point[0], end_point[0], num), np.linspace(start_point[1], end_point[1], num)
    image2=draw_on_image(image2, start_point,end_point)
    # Get the grayscale values along the line
    gray_values = image[x.astype(int),y.astype(int)]
    linecut=[]
    for i in range(len(gray_values)):
        linecut_value=np.sqrt((gray_values[i][0])**2+(gray_values[i][1])**2+(gray_values[i][2])**2)
        linecut.append(linecut_value)
        
    return(np.array(linecut),image2)

#plt.imshow(image)


for i in range(len(theta)):
    x1=round(x+radius*np.sin(theta[i]))
    y1=round(y-radius*np.cos(theta[i]))
    
    x2=round(x-radius*np.sin(theta[i]))
    y2=round(y+radius*np.cos(theta[i]))
    
    start_point=[x1,y1]
    end_point=[x2,y2]
    linecut,image2=linecut_function(start_point,end_point,image,image2)
    plt.plot(linecut)
    plt.title("pixel no: (%d"%x+",%d"%y+")    theta=%d"%(theta_degree[i]))
    plt.xlabel('start: %d'%start_point[0]+',%d'%start_point[1]+'\n end: %d'%end_point[0]+',%d'%end_point[1])
    plt.show()

image2=np.asarray(image2)
plt.imshow(image2)