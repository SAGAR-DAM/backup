# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 18:57:13 2023

@author: mrsag
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as fit
from decimal import Decimal

def Lorentzian(x,a,b,x0):
    y=a/(b**2+(x-x0)**2)
    return y

def Lorentzfit(w,I):
    xdata=w
    ydata=I
    ymax_index=(list(ydata)).index(max(ydata))
    xmax_val=xdata[ymax_index]
    xdata=xdata-xmax_val
    parameters, covariance = fit(Lorentzian, xdata, ydata,maxfev=100000)
    fit_y = Lorentzian(xdata, *parameters)

    
    xdata=xdata+xmax_val
    parameters[2]+=xmax_val
    
    fit_y=np.asarray(fit_y)
    
    string1=r"Fit: f(x)=$\frac{a}{b^2+(x-x_0)^2}$; "
    string2=rf"with a={Decimal(str(parameters[0])).quantize(Decimal('1.00'))}, b={Decimal(str(parameters[1])).quantize(Decimal('1.00'))}, $x_0$={Decimal(str(parameters[2])).quantize(Decimal('1.00'))}"
    string=string1+string2

    return fit_y,parameters,string

def main():
    #Lorentzisn demo fit
    x=np.linspace(-20,20,201)      #data along x axis
    y=50/(5+(x-2)**2)             #data along y axis
    random_noise=np.random.uniform(low=-1,high=1,size=(len(y)))
    y=y+random_noise
    
    fit_y,parameters,string=Lorentzfit(x,y)
    plt.plot(x,y,'ko')
    plt.plot(x,fit_y)
    print(string)
    plt.title(string)
    plt.show()
    
    print(*parameters)
    print('FWHM= ', 2*parameters[1])
    
if __name__=='__main__':
    main()