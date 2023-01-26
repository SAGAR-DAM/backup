# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 23:01:38 2023

@author: mrsag
"""

#julia set python code
import numpy as np
import matplotlib.pyplot as plt

# Set the number of iterations
n_iter = 200

# Create a grid of x and y values
x = np.linspace(-2, 2, 500)
y = np.linspace(-2, 2, 500)
X, Y = np.meshgrid(x, y)

# Convert x and y values to complex numbers
Z = X + 1j*Y

# Initialize the output array
output = np.zeros(Z.shape)
#output = output+n_iter    # for the reverse image

# Iterate over each complex number
for i in range(n_iter):
    Z = Z*Z + ( -0.8 + 0.156j)
    output[np.abs(Z) < 1] = i

# Plot the output
plt.figure(figsize=(30,20))
plt.imshow(output, cmap='hot')
plt.axis('off')
plt.colorbar()
plt.show()

#print(output)
#print(output.shape)
#print(Z)
#print(np.abs(Z))