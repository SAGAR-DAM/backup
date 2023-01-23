# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import matplotlib.pyplot as plt
from skimage import io

'''     INPUTS     '''

image = io.imread('D:\\pictures\\DSCN4281.JPG')
colour='green'   # Inputs: red, green, blue, yellow, magenta, cyan


#print(image.shape)

def colour_filtering(image,colour):
    matrix=[[[0,0,0]]*image.shape[1]]*image.shape[0]
    matrix=np.array(matrix)
    #print(matrix.shape)
    
    if(colour=='red'):
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                red=image[i][j][0]
                green=image[i][j][1]
                blue=image[i][j][2]
                #matrix[i,j]=y
                matrix[i,j][0]=red
                matrix[i,j][1]=0
                matrix[i,j][2]=0    
                
    elif(colour=='green'):
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                red=image[i][j][0]
                green=image[i][j][1]
                blue=image[i][j][2]
                #matrix[i,j]=y
                matrix[i,j][0]=0
                matrix[i,j][1]=green
                matrix[i,j][2]=0
                
    elif(colour=='blue'):
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                red=image[i][j][0]
                green=image[i][j][1]
                blue=image[i][j][2]
                #matrix[i,j]=y
                matrix[i,j][0]=0
                matrix[i,j][1]=0
                matrix[i,j][2]=blue
                
    elif(colour=='yellow'):
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                red=image[i][j][0]
                green=image[i][j][1]
                blue=image[i][j][2]
                #matrix[i,j]=y
                matrix[i,j][0]=red
                matrix[i,j][1]=green
                matrix[i,j][2]=0
                
    elif(colour=='magenta'):
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                red=image[i][j][0]
                green=image[i][j][1]
                blue=image[i][j][2]
                #matrix[i,j]=y
                matrix[i,j][0]=red
                matrix[i,j][1]=0
                matrix[i,j][2]=blue
                
    elif(colour=='cyan'):
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                red=image[i][j][0]
                green=image[i][j][1]
                blue=image[i][j][2]
                #matrix[i,j]=y
                matrix[i,j][0]=0
                matrix[i,j][1]=green
                matrix[i,j][2]=blue
    
    return(matrix)

matrix=colour_filtering(image, colour)
plt.figure(figsize=(30,20))
plt.imshow(matrix)