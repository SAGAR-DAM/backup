# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 16:23:17 2023

@author: sagar
"""
import Three_Gaussian_Fitting as tgft
import numpy as np
import matplotlib.pyplot as plt
import glob
from skimage import io, feature
from skimage.color import rgb2gray, rgba2rgb
from PIL import Image, ImageDraw
from scipy.stats import gmean


import matplotlib
matplotlib.rcParams['figure.dpi']=300 # highres display


def draw_on_image(image,x,y):             #function  to draw a line on the image for two given points
    draw = ImageDraw.Draw(image)
    draw.line((x[1],x[0],y[1],y[0]), fill=(255, 0, 0), width=1)
    return(image)


def linecut_function(start_point,end_point,image,image2):     #function to give the linecut along the line between two given points
    # Use the numpy function linspace to get the coordinates of the line
    num=round(np.sqrt((start_point[0]-end_point[0])**2+(start_point[1]-end_point[1])**2))      #number of pixels between these two points
    x, y = np.linspace(start_point[0], end_point[0], num), np.linspace(start_point[1], end_point[1], num)     #pixels along x and y
    image2=draw_on_image(image2, start_point,end_point)   #drawing the line between the given points
    # Get the grayscale values along the line
    gray_values = image[x.astype(int),y.astype(int)]
    linecut=[]
    for i in range(len(gray_values)):
        linecut_value=np.sqrt((gray_values[i][0])**2+(gray_values[i][1])**2+(gray_values[i][2])**2)   # taking the grey values along the linecut line
        linecut.append(linecut_value)
        
    return(np.array(linecut),image2)      # return back the linecut array and the image with lines along the linecuts


def brightest(image):
    # Find the coordinates of the brightest point using the corner_peaks function
    if(image.ndim==2):
        coords = feature.corner_peaks(np.abs(image), min_distance=10)
    elif(image.ndim==3):
        if(image.shape[2]==3):
            coords = feature.corner_peaks(np.abs(rgb2gray(image)), min_distance=10)
        elif(image.shape[2]==4):
            coords = feature.corner_peaks(np.abs(rgba2rgb(rgb2gray(image))), min_distance=10)
    return(coords[0])
    
def main():
    files=glob.glob("D:\\Codes\\Test folder\\images\\*.bmp")
    pixel_size=2.3
    
    all_fwhm_list=[]
    
    for i in range(len(files)):
        print(files[i])
        image = io.imread(files[i])
        image2 = Image.open(files[i])
        
        point=brightest(image)
        
        #####################################################################################
        radius=90          # the radius of the circle in which the linecuts are drawn
        x=point[0]         #x coordinate (row of the matrix)
        y=point[1]         #y coordinate (column of the matrix)
    
        X=image.shape[0]-1       #image size in x direction
        Y=image.shape[1]-1       #image size in y direction
    
        boundary_distances=[x,y,X-x,Y-y]    # distances of boundary from the given point
    
        #radius=min(boundary_distances)
    
        #####################################################################################
        theta_degree=np.linspace(0,150,6)    # angels, for which the linecuts will be drawn
        theta=theta_degree*np.pi/180          # angels in radian
        FWHM=[]                 
        ####################################################################################
        functional_form=r"$\sum_{i=1}^3A_ie^{-\frac{(x-x_{0i})^2}{2b^2_i}}$"
        ####################################################################################
        
        #plt.imshow(image)
        #plt.show()
        filename_at_caption=(files[i]).replace("D:\\Codes\\Test folder\\images\\","")
        print(filename_at_caption)
        
        
        for j in range(len(theta)):
            x1=round(x+radius*np.sin(theta[j]))
            y1=round(y-radius*np.cos(theta[j]))
            
            x2=round(x-radius*np.sin(theta[j]))
            y2=round(y+radius*np.cos(theta[j]))
            
            start_point=[x1,y1]
            end_point=[x2,y2]
            linecut,image2=linecut_function(start_point,end_point,image,image2)   #getting the linecut along the start and end points
            linecut=linecut/linecut.max()   #normalizing the linecut grey values
            
            fit_linecut,parameters=tgft.Multi_Gaussfit(np.arange(len(linecut)),linecut)    #Gaussian fit for the linecut
            fwhm=2.355*(parameters[1]+parameters[3]*parameters[4]+parameters[6]*parameters[7])    # getting the FWHM along the linecut
            FWHM.append(fwhm)
            
            FWHM_round=[]
            for i in range(len(FWHM)):
                fwhm_round=round(FWHM[i],2)
                FWHM_round.append(fwhm_round)
                
                
            plt.plot(linecut,'ro-',markersize=5,label='linecut')
            plt.plot(fit_linecut,'k-',label='Multi-Gaussian fit')
            plt.legend()
            plt.grid()
            plt.figtext(0.95,0.1,("Fit Function:\n%s"%functional_form+"\n___________________\n\nParameters:\n"+str(parameters)),fontname="Times New Roman")
            plt.title("Normalized Linecut at:\npixel no: (%d"%x+",%d"%y+")    theta=%d"%(theta_degree[j])+"\n of image: %s"%filename_at_caption,fontname="Times New Roman")
            plt.xlabel('Pixel no \nstart: (%d'%start_point[0]+',%d'%start_point[1]+')      end: (%d'%end_point[0]+',%d'%end_point[1]+")\n FWHM = %f"%fwhm+" Pixels /  %f"%(pixel_size*fwhm)+" micron",fontname="Times New Roman")
            plt.ylabel("Relative intensity",fontname="Times New Roman")
            plt.show()
    
        image2=np.asarray(image2)
        
        plt.figure()
        plt.imshow(image2[x-radius:x+radius,y-radius:y+radius])
        plt.title("%s"%filename_at_caption,fontname="Times New Roman")
        #plt.xlabel(f"fwhm list: {FWHM_round}\nAverage FWHM from all directions: %f"%np.mean(FWHM))
        plt.xlabel("Average FWHM from all directions: %f"%(pixel_size*gmean(FWHM))+" micron",fontname="Times New Roman")
        #plt.savefig("D:\\data Lab\\Supercontinuum-march 2023\\10th march 2023\\Focal spot measurement\\Draw on images\\%s.jpg"%filename_at_caption,bbox_inches='tight')
        plt.show()
        #print("Average FWHM from all directions: ", np.mean(FWHM))
        
        all_fwhm_list.append(gmean(FWHM))
        
    
    all_fwhm_list=np.array((all_fwhm_list))
    print("_____________________________________________________________________________________")
    print(f"FWHM of differnet images: {pixel_size*all_fwhm_list}")
    print("_____________________________________________________________________________________")
    print(f"Min spot size: {min(all_fwhm_list)} pixels / {pixel_size*min(all_fwhm_list)} micron")
    print("_____________________________________________________________________________________")
    print(f"Focal Spot area:\n{np.pi*(pixel_size*min(all_fwhm_list))**2/4} micron^2")
    print(f"{10**(-8)*np.pi*(pixel_size*min(all_fwhm_list))**2/4} cm^2")
        
if __name__=='__main__':
    main()