# -*- coding: utf-8 -*-
"""
Created on Wed May 22 22:18:32 2024

@author: mrsag
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

import matplotlib as mpl

mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Times New Roman'
mpl.rcParams['font.size'] = 12
#mpl.rcParams['font.weight'] = 'bold'
#mpl.rcParams['font.style'] = 'italic'  # Set this to 'italic'
mpl.rcParams['figure.dpi'] = 300  # highres display


def polynomial_fit(x,y,degree):
    ''' Will take two 1 d arrays x and y and the required degree of 
    fitting and will return the fitted curve along with the fitting coefficients.
    
    y = c0 + c1*x + c2*x**2 + c3*x**3 + ...
    
    the return will be y_predict curve and coefficient array: [c0,c1,c2,c3,...]'''
    
    x = x[:,np.newaxis]
    y = y[:,np.newaxis]

    model = make_pipeline(PolynomialFeatures(degree), linear_model.LinearRegression(fit_intercept=False))

    # Train the model using the training sets
    model.fit(x, y)

    # Make predictions using the testing set
    y_predict = model.predict(x)
    
    # Access the linear regression model within the pipeline
    linear_reg_model = model.named_steps['linearregression']
    
    return y_predict, (linear_reg_model.coef_).flatten()


# # Extract features
# age = np.random.uniform(low=-10, high=10, size = 1000)


# # Target variable
# #f = 150-50*age-100*np.sin(age)+2*age**2+age**3+100*np.random.uniform(low=-1, high=1, size=len(age))
# f = 100-10*age+20*age**2+3*age**3+100*np.random.uniform(low=-1, high=1, size=len(age))
# #f = np.sin(age)+0.2*np.random.uniform(low=-1, high=1, size=len(age))
# degree = 3

# f_predict, coefficients = polynomial_fit(age, f, degree)

# print(coefficients)

# sorted_indices = np.argsort(age)
# age = age[sorted_indices]
# f = f[sorted_indices]
# f_predict = f_predict[sorted_indices]

# plt.scatter(age,f)
# plt.plot(age,f_predict,'r-')
# plt.show()