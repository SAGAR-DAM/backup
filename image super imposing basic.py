# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 18:51:38 2023

@author: Sagar Dam

This code takes two images (of same dimensions) as input and gives the overlapped/ superimposed image as a ratio of 50:50 
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from PIL import Image, ImageDraw

# Load the image
image1_path='D:\\pictures\\DSCN4281.JPG'
image2_path='D:\\pictures\\DSCN4282.JPG'
image1 = io.imread(image1_path)
image2 = io.imread(image2_path)

print(image1.shape)
print(image2.shape)

matrix=[[[0,0,0]]*image1.shape[1]]*image1.shape[0]
matrix=np.array(matrix)
print(matrix.shape)

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        red1=image1[i][j][0]
        green1=image1[i][j][1]
        blue1=image1[i][j][2]
        
        red2=image2[i][j][0]
        green2=image2[i][j][1]
        blue2=image2[i][j][2]
        
        red_mean=int(red1/2)+int(red2/2)
        green_mean=int(green1/2)+int(green2/2)
        blue_mean=int(blue1/2)+int(blue2/2)
        #matrix[i,j]=y
        '''matrix[i,j][0]=int(red1)
        matrix[i,j][1]=int(green1)
        matrix[i,j][2]=int(blue1)'''

        matrix[i,j][0]=red_mean
        matrix[i,j][1]=green_mean #green_mean
        matrix[i,j][2]=blue_mean #blue_mean
        
#print(matrix)

plt.figure(figsize=(30,20))
plt.axis('off')
plt.imshow(matrix)
