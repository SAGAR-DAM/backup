# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 18:57:13 2023

@author: mrsag
"""
"""
This is the fitting function for Double Gaussian data. The inputs are two same length array of datatype float.
There are 3 outputs:
1. The array after fitting the data. That can be plotted.
2. The used parameters set as the name parameters.
3. The string to describe the parameters set and the fit function.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as fit
from decimal import Decimal
import pandas as pd 

import matplotlib
matplotlib.rcParams['figure.dpi']=300 # highres display

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


def Multi_Gaussfit(x,y):
    fit_y1,parameters1,string1=Gaussfit(x,y)

    y2=y-fit_y1
    fit_y2,parameters2,string2=Gaussfit(x,y2)
    
    y3=y-fit_y1-fit_y2
    fit_y3,parameters3,string3=Gaussfit(x,y3)
    
    fit_y=fit_y1+fit_y2+fit_y3
    
    parameters_data=[max(fit_y1),parameters1[0],parameters1[1],max(fit_y2),parameters2[0],parameters2[1],max(fit_y3),parameters3[0],parameters3[1]]
    parameters_name=[r"$A_1$",r"$\sigma_1$",r"$x_{01}$",r"$A_2$",r"$\sigma_2$",r"$x_{02}$",r"$A_3$",r"$\sigma_3$",r"$x_{03}$"]
    
    parameters=pd.Series(parameters_data,index=parameters_name)
    
    return(fit_y,parameters)    
'''
x=np.linspace(-10,30,401)      #data along x axis
y=50*np.exp(-(x-0)**2/5)+30*np.exp(-(x-10)**2/7)+10*np.exp(-(x-20)**2/50)            #data along y axis
random_noise=np.random.uniform(low=-2,high=2,size=(len(y)))
y=y+random_noise

fit_y,parameters=Multi_Gaussfit(x, y)
print(parameters)



plt.figure()
plt.plot(x,y,color='k')
#plt.title(string)
plt.plot(x,fit_y,'b-')
plt.figtext(0.95,0.2,str(parameters))
#plt.plot(x,y2,'r-')
plt.show()

#print(*parameters)
#print('FWHM= ', 2.355*parameters[0])
'''