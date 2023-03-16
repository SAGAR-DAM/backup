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
    
    print(r"For the form of f(x)=$e^{-\frac{(x-x_0)^2}{2b^2}}$ the normalized gaussian fitting is")
    return fit_y,parameters



def main():
    x=np.linspace(-20,20,201)      #data along x axis
    y=10*np.exp(-(x-0)**2/5)             #data along y axis
    random_noise=np.random.uniform(low=-0.4,high=0.4,size=(len(y)))
    y=y+random_noise
    
    fit_y,parameters=Gaussfit(x,y)
    plt.plot(x,y,'ko')
    plt.plot(x,fit_y)
    plt.show()
    
    print(*parameters)
    print('FWHM= ', 2.355*parameters[0])
    
    
if __name__=='__main__':
    main()