# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:00:24 2022

@author: SAGAR DAM

"""
#######################################################
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import os
import numba
#######################################################

##########################################################
##########################################################
##########################################################
##########################################################
#               '''Scan 1 - forward'''
##########################################################
##########################################################
##########################################################
##########################################################

timelimit=0  #delay time range
filenumber=1300   #total number of files
delay=np.arange(-timelimit,timelimit,filenumber)   #array for delay range

wavelength=[[0]*2048]*filenumber   # wavelength matrix 
intensity=[[0]*2048]*filenumber    # intensity matrix (i th file, j th wavelength value) 

wavelength=np.matrix(wavelength)  
intensity=np.matrix(intensity)
#######################################################

# reading values from files 

for i in range(0,9):
    f=open("Scan 1 - forward\data_00%d.txt"% (i))  #read with file name
    r=np.loadtxt(f,skiprows=17,comments=">")  #load text from that file

    lamb=r[:,0]   #first coloumn as wavelength
    intense=r[:,1]    #second coloumn as intensity (got spectrum)
    intense[0]=intense[1]  #as the 0'th value was junk as 0
    for j in range(len(lamb)):   #putting value at the intensity matrix
        intensity[i,j]=intense[j]
    #plt.figure(figsize=(30,15))
    plt.plot(lamb,intense,'r-')   #plot the spectrum for i'th file (delay)
    
########################################################    

for i in range(10,99):
    f="Scan 1 - forward\data_0%d.txt"% (i)   #read with file name
    r=np.loadtxt(f,skiprows=17,comments=">")   #load text from that file

    lamb=r[:,0]
    intense=r[:,1]
    intense[0]=intense[1]
    for j in range(len(lamb)):
        intensity[i,j]=intense[j]
    #plt.figure(figsize=(30,15))
    plt.plot(lamb,intense,'r-')
    
########################################################

for i in range(100,999):
    f="Scan 1 - forward\data_%d.txt"% (i)
    r=np.loadtxt(f,skiprows=17,comments=">")

    lamb=r[:,0]
    intense=r[:,1]
    intense[0]=intense[1]
    for j in range(len(lamb)):
        intensity[i,j]=intense[j]
    #plt.figure(figsize=(30,15))
    plt.plot(lamb,intense,'r-')
    
#########################################################
    
for i in range(1000,filenumber):
    f="Scan 1 - forward\data_%d.txt"% (i)
    r=np.loadtxt(f,skiprows=17,comments=">")

    lamb=r[:,0]
    intense=r[:,1]
    intense[0]=intense[1]
    for j in range(len(lamb)):
        intensity[i,j]=intense[j]
    #plt.figure(figsize=(30,15))
    plt.plot(lamb,intense,'r-')
    

plt.title("spectrums for all delays", size=20)
plt.xlabel("wavelength (nm)",size = 15)
plt.ylabel("Intensity (arb unit)", size = 15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(fontsize=15)    
plt.show()  #showing all the spectrum plots

#########################################################
#########################################################
  
xlambda=lamb  #all the wavelength values in meshgrid
fname=np.arange(filenumber)   #array: 1,2,3,..., total number of delays
lname=np.arange(len(lamb))   #array: 1,2,3,..., total number of wavelength values
delay=np.linspace(-10,10,len(fname))  #array for delay values


fint,lint=np.meshgrid(delay,xlambda)   #meshgrid (delay,wavelength) in values
Fint,Lint=np.meshgrid(fname,lname)   #meshgrid [1,2,3,...,total number of delays][1,2,3,...,total number of wavelength values]

#########################################################
#########################################################

def F(i,j):  #function to put values in meshgrid as function of delay and wavelength
    return intensity[i,j]  #return from intensity matrix (previously taken)

I=F(Fint,Lint)  #3rd axis of meshgrid 


plt.contourf(fint,lint,I, 20, cmap='RdGy')  #contour plot
plt.title("Contour plot of intensities as function of wavelength and delay", size=20)
plt.xlabel("delay (ps)", size=15)
plt.ylabel("wavelength (nm)", size=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.colorbar();
plt.show() 