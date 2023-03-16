# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 18:57:13 2023

@author: mrsag
"""
"""
This is the fitting function for Gaussian data. The inputs are two same length array of datatype float.
There are 3 outputs:
1. The array after fitting the data. That can be plotted.
2. The used parameters set as the name parameters.
3. The string to describe the parameters set and the fit function.
"""

import numpy as np
#import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as fit
from decimal import Decimal

def Gauss1(x,b,x0):
    y=np.exp(-(x-x0)**2/(2*b**2))
    return y

def Gaussfit(w,I):
    xdata=w         #Taking the x axis data
    ydata=I         #Taking the y axis data
    
    ''' 
        here the code fits only the normalized Gaussian
        So, we first normalize the array and later multiply with the amplitude factor to get the main array
    '''
    y_maxval=max(ydata)      #taking the maximum value of the y array
    ymax_index=(list(ydata)).index(y_maxval)   
    
    xmax_val=xdata[ymax_index]  #Shifting the array as a non-shifted Gausian 
    xdata=xdata-xmax_val        #Shifting the array as a non-shifted Gausian
    
    ydata=ydata/y_maxval
    
    parameters, covariance = fit(Gauss1, xdata, ydata,maxfev=100000)
    fit_y = Gauss1(xdata, *parameters)
    
    
    xdata=xdata+xmax_val
    parameters[1]+=xmax_val
    
    fit_y=np.asarray(fit_y)
    fit_y=fit_y*y_maxval       # again multiplying the data to get the actual value
    
    string1=r"Fit: $f(x)=Ae^{-\frac{(x-x_0)^2}{2b^2}}$;"
    string2=rf"with A={Decimal(str(y_maxval)).quantize(Decimal('1.00'))}, b={Decimal(str(parameters[0])).quantize(Decimal('1.00'))}, $x_0$={Decimal(str(parameters[1])).quantize(Decimal('1.00'))}"
    string=string1+string2
    return fit_y,parameters,string

'''
x=np.linspace(0,20,201)      #data along x axis
y=10*np.exp(-(x-2.564)**2/5)             #data along y axis
random_noise=np.random.uniform(low=-1,high=1,size=(len(y)))
y=y+random_noise

fit_y,parameters=Gaussfit(x,y)
plt.plot(x,y,color='k')
plt.plot(x,fit_y)
plt.show()

print(*parameters)
print('FWHM= ', 2.355*parameters[0])
'''