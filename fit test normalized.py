# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 11:32:58 2022

@author: mrsag
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the Gaussian function
'''
def function(x,b,a,x0):
    y=(b**2)/(a**2+(x-x0)**2)
    return y
'''
def function1(x,a,b,x0):
    y=np.exp(-b*(x-x0)**2)
    return y

def function2(x,a,b,x0):
    y=np.exp(-b*(x+x0)**2)
    return y

def function_fit(w,I):
    xdata=np.asarray(w[minval:maxval])
    ydata=np.asarray(I[minval:maxval])

    ymax_index=(list(ydata)).index(max(ydata))
    xmax_val=xdata[int(len(xdata)/2)]
    xdata=xdata-xmax_val
    #ymin_val=min(ydata)
    ymin_val=np.average(I[100:500])
    ydata=ydata-ymin_val
    ydata=ydata/max(ydata)
    
    if ymax_index>=int(len(xdata)/2):
        parameters, covariance = curve_fit(function1, xdata, ydata,maxfev=100000)
        fit_y = function1(xdata, *parameters)
    
    if ymax_index<int(len(xdata)/2):
        parameters, covariance = curve_fit(function2, xdata, ydata,maxfev=100000)
        fit_y = function2(xdata, *parameters)
        
    
    #fit_y=fit_y+ymin_val
    offset=fit_y[0]-ydata[0]
    #fit_y=fit_y-offset
    
    xdata=xdata+xmax_val
    fit_y=np.asarray(fit_y)
    
    return xdata,fit_y,parameters

file=[]
for i in range(132):
    file.append(i+1)

f=open("D:\\python files\\2d doppler new\\Data\\01.txt")
r=np.loadtxt(f)


minval=1800            # peak=[1800:1970]
maxval=1970            # len(w)=3648
#print(maxval)

'''
for j in range(1):
    w=r[:,2*j]
    I=r[:,2*j+1]
    xdata,fit_y,p=function_fit(w,I)
    if p[1]>0:
        Imax=max(fit_y)
        I_index_imax=(list(fit_y)).index(Imax)
        x_Imax_val=xdata[I_index_imax]
    plt.plot(w[minval:maxval],I[minval:maxval],label="S%d"%(1+j))
    plt.legend()
    plt.plot(xdata,fit_y)
    plt.show()
    

'''
count=0


for i in range(len(file)):
    
    if(file[i]<10):
        f=open("D:\\python files\\2d doppler new\\Data\\0%d.txt"% (file[i]))  # read the data
    if(file[i]>=10):
        f=open("D:\\python files\\2d doppler new\\Data\\%d.txt"% (file[i]))  # read the data
   
    r=np.loadtxt(f)


    for j in range(16):
        w=np.asarray(r[:,2*j])
        I=np.asarray(r[:,2*j+1])
        if max(I[minval:maxval])>200:
            xdata,fit_y,p=function_fit(w,I)
            if p[1]>0:
                Imax=max(fit_y)
                I_index_imax=(list(fit_y)).index(Imax)
                x_Imax_val=xdata[I_index_imax]
                
            plt.figure()
            plt.title("Filenumber %d"%file[i],fontname="cursive",fontweight="bold",color='green')
            
            # Unnormalized plot
            plt.plot(w[minval:maxval],I[minval:maxval],label="S%d"%(1+j),linewidth=5)
            plt.plot(xdata,fit_y*max(I[minval:maxval]),linewidth=5)
            
            # Normalized plot
            #plt.plot(w[minval:maxval],I[minval:maxval]/max(I[minval:maxval]),label="S%d"%(1+j))
            #plt.plot(xdata,fit_y)
            plt.xlabel("Wavelength (nm)",fontname="Times New Roman",fontweight="light")
            plt.ylabel("Intensity (arb unit)",fontname="Times New Roman",fontweight="light")
            plt.xticks(color='purple')
            plt.yticks(color='purple')
            plt.legend()
            plt.grid()
            plt.savefig('D:\\python files\\2d doppler new\\plots 2 unnormalized\\s (%d'%(1+j)+')\\file %d.jpg'%(file[i]))
            plt.show()
            
            count=count+1
            

print(count)        