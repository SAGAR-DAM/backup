# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import matplotlib.pyplot as plt
from skimage import io,img_as_ubyte

image = img_as_ubyte(io.imread('D:\\pictures\\DSCN4281.JPG',as_gray=True))  #Read the image in greyscale format
#image = img_as_ubyte(io.imread('D:\\data Lab\\frog\\Granouille allignment\\16jan2023\\ids raw\\5_33.png',as_gray=True))
print(image.shape)


grating=image 

plt.set_cmap='grey'
plt.figure(num=None, figsize=(30, 22), dpi=80)

plt.subplot(131)
plt.imshow(grating)
plt.axis("off")

# Calculate the Fourier transform of the grating
ft = np.fft.fftshift(grating)
ft = np.fft.fft2(ft)
ft = np.fft.fftshift(ft)

plt.subplot(132)
plt.imshow(np.log(abs(ft)))
plt.axis("off")
#plt.xlim([480, 520])
#plt.ylim([520, 480])

# Calculate the inverse Fourier transform of 
# the Fourier transform
ift = np.fft.ifftshift(ft)
ift = np.fft.ifft2(ift)
ift = np.fft.ifftshift(ift)
ift = ift.real  # Take only the real part

plt.subplot(133)
plt.imshow(ift)
plt.axis("off")
plt.show()

print(grating)