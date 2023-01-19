# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 12:04:57 2022

@author: Sagar Dam

2D Doppler data processing code
"""

############################################################################################################
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as fit
############################################################################################################

timedelay=0
filenumber=132
spectrometernumber=16
threshhold=300
file=[]
lw=5

############################################################################################################

def Gauss1(x,a,b,x0):
    y=np.exp(-b*(x-x0)**2)
    return y

def Gauss2(x,a,b,x0):
    y=np.exp(-b*(x+x0)**2)
    return y

def Gaussfit(w,I):
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
        parameters, covariance = fit(Gauss1, xdata, ydata,maxfev=100000)
        fit_y = Gauss1(xdata, *parameters)
   
    if ymax_index<int(len(xdata)/2):
        parameters, covariance = fit(Gauss2, xdata, ydata,maxfev=100000)
        fit_y = Gauss2(xdata, *parameters)
    #fit_y=fit_y+ymin_val
    offset=fit_y[0]-ydata[0]
    #fit_y=fit_y-offset
    
    xdata=xdata+xmax_val
    fit_y=np.asarray(fit_y)
    
    return xdata,fit_y,parameters

for i in range(132):
    file.append(i+1)

minval=1800            # peak=[1800:1970]
maxval=1970            # len(w)=3648

spec_fit=[]
for i in range(16):
    spec_fit.append([])
    

# MAIN LOOP
for i in range(len(file)):
    w=[]
    I=[]
    count=0
    
    if(file[i]<10):
        f=open("D:\\python files\\2d doppler new\\Data\\0%d.txt"% (file[i]))  # read the data
    if(file[i]>=10):
        f=open("D:\\python files\\2d doppler new\\Data\\%d.txt"% (file[i]))  # read the data
    r=np.loadtxt(f)
    
    plt.figure(figsize=(40,28))  
    plt.title("Filenumber %d"%file[i],size=75,fontname="cursive",fontweight="bold",color='green')
    
    for j in range(spectrometernumber):
        w1=np.asarray(r[:,2*j])
        I1=np.asarray(r[:,2*j+1])
        w.append(w1)
        I.append(I1)
        
        for k in range(len(w[j])):
            if(I[j][k]<0):
                I[j][k]=0
                                
        if(max(I[j][minval:maxval])>threshhold):
            xdata,fit_y,p= Gaussfit(w[j],I[j])
            
            # Normalized Plot 
            plt.plot(w[j][minval:maxval],I[j][minval:maxval]/max(I[j][minval:maxval]),label='s%d'%(1+j),linewidth=lw) 
            plt.plot(xdata,fit_y,'-',label='fit s%d'%(1+j),linewidth=lw)
            
            # Unnormalized plot
            #plt.plot(w[j][minval:maxval],I[j][minval:maxval],label="S%d"%(1+j),linewidth=5)
            #plt.plot(xdata,fit_y*max(I[j][minval:maxval]),linewidth=5)
            
            count=count+1
            
            if(p[1]>0):
                Imax=max(fit_y)
                I_index_imax=(list(fit_y)).index(Imax)
                x_Imax_val=xdata[I_index_imax]
                #sp1_fit.append(x_Imax_val)
                spec_fit[j].append(x_Imax_val)
                
    plt.xlabel("Wavelength (nm)",fontname="Times New Roman",fontweight="light",fontsize=60)
    plt.ylabel("Intensity (arb unit)",fontname="Times New Roman",fontweight="light",fontsize=60)
    plt.figtext(0.15,0.8,"Count: %d"%count,fontname="Times New Roman",fontweight="light",fontsize=60)
    plt.xticks(fontsize=45,color='purple')
    plt.yticks(fontsize=45,color='purple')
    plt.legend(fontsize=45)
    plt.grid()
    #plt.savefig('D:\\python files\\2d doppler new\\plots normalized\\file %d.jpg'%(file[i]))
    plt.show()
    
plt.figure(figsize=(40,28))
plt.title("delay vs shift",size=75,fontname="cursive",fontweight="bold",color='green')
    
for i in range(spectrometernumber):
    delay=np.arange(len(spec_fit[i]))
    plt.plot(delay,spec_fit[i],'o-',label='s%d'%(1+i),linewidth=lw)

plt.xlabel("delay",fontname="Times New Roman",fontweight="light",fontsize=60)
plt.ylabel("wavelength shift",fontname="Times New Roman",fontweight="light",fontsize=60)
plt.xticks(fontsize=45,color='purple')
plt.yticks(fontsize=45,color='purple')
plt.legend(fontsize=45)
plt.grid()
plt.show()