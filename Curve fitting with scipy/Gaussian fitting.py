# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 18:57:13 2023

@author: mrsag
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as fit

def Gauss1(x,b,x0):
    y=np.exp(-(x-x0)**2/(2*b**2))
    return y

def Gaussfit(w,I):
    xdata=w
    ydata=I
    ymax_index=(list(ydata)).index(max(ydata))
    xmax_val=xdata[ymax_index]
    xdata=xdata-xmax_val
    parameters, covariance = fit(Gauss1, xdata, ydata,maxfev=100000)
    fit_y = Gauss1(xdata, *parameters)

    
    xdata=xdata+xmax_val
    fit_y=np.asarray(fit_y)
    
    return fit_y,parameters

x=np.linspace(0,20,201)      #data along x axis
y=1/(1+(x-5)**2)             #data along y axis

fit_y,parameters=Gaussfit(x,y)
plt.plot(x,y,color='k')
plt.plot(x,fit_y)
plt.show()

print(*parameters)
print('FWHM= ', 2.355*parameters[0])