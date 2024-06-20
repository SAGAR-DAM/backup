# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 20:06:55 2024

@author: mrsag
"""

from diffractsim import ApertureFromFunction, ApertureFromImage, MonochromaticField, mm, cm, nm, um
from diffractsim import Lens, GaussianBeam
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import map_coordinates
from skimage import io
from skimage.transform import resize
import imageio
import types

import matplotlib as mpl

mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Times New Roman'
mpl.rcParams['font.size'] = 12
#mpl.rcParams['font.weight'] = 'bold'
#mpl.rcParams['font.style'] = 'italic'  # Set this to 'italic'
mpl.rcParams['figure.dpi'] = 300  # highres display

##############################################################################
##############################################################################
##############################################################################
##############################################################################

def find_index(array, value):
    # Calculate the absolute differences between each element and the target value
    array = np.abs(array)
    absolute_diff = np.abs(array - value)
    # Find the index of the minimum absolute difference
    index = np.argmin(absolute_diff)
    return index

def intensity_linecut(intensity):
    global field
    I_line = intensity[(intensity.shape[1])//2,:]
    I_line /= max(I_line)
    plt.plot(field.xx[0,:]/mm,I_line,'r-',lw=1)
    plt.title("Intenasity variation across screen centre")
    plt.xlabel("x (mm)")
    plt.ylabel(r"I$_{norm}$   (Arb unit)")
    plt.show()
    pass


##############################################################################
##############################################################################
##############################################################################
##############################################################################

# Create a monochromatic field with a specific wavelength
wavelength = 800 * nm  # Wavelength of 500 nm
field = MonochromaticField(
    wavelength=wavelength,
    extent_x=10*mm,
    extent_y=10*mm,
    Nx=1024,
    Ny=1024
)

# Define the initial beam waist
beam_waist = 1.5 * mm
field.add(GaussianBeam(w0=beam_waist))

intensity = field.get_intensity()
intensity /= np.max(intensity)
field.plot_intensity(intensity)
intensity_linecut(intensity)


## Target P0sition

x_shift = -150
y_shift = -200

savegif = False

##############################################################################
##############################################################################
##############################################################################
##############################################################################

USAF = io.imread("D:\\Codes\\lab codes\\Diffraction pattern\\USAF-1951.png",as_gray=True)
USAF = np.array(USAF)
USAF = (USAF>0.8)
USAF = (1-USAF)
USAF = USAF[50:1610,55:1700]
USAF = resize(USAF, (2000,2000), anti_aliasing=True)

a = 130
usaf = resize(USAF,(a,a),anti_aliasing=True)
USAF[1100:1100+a,1100:1100+a] = usaf
del usaf

def f(x, y, wavelength):
    global USAF
    height, width = USAF.shape[:2]
    x_img = ((x - x.min()) / (x.max() - x.min()) * (width - 1)).astype(int)
    y_img = ((y - y.min()) / (y.max() - y.min()) * (height - 1)).astype(int)
    
    return (np.roll(np.roll(USAF, x_shift, axis=1), y_shift, axis=0))[y_img, x_img]

# Create the aperture pattern
x = field.xx
y = field.yy

# Plot the aperture pattern
plt.figure()
plt.imshow(USAF, extent=(x.min()/mm, x.max()/mm, y.min()/mm, y.max()/mm), cmap='gray')
plt.title('Aperture Pattern (Circular Holes)')
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.colorbar(label='Transmittance')
plt.show()



##############################################################################
##############################################################################
##############################################################################
##############################################################################

# Define the first lens
focal_length_1 = 50 * mm  # Focal length of the first lens
lens1 = Lens(f=focal_length_1, radius= 10*beam_waist)
field.add(lens1)
field.propagate(30 * mm)

# Create an aperture from the function
aperture = ApertureFromFunction(f)
# Add the aperture to the field
field.add(aperture)


intensity = field.get_intensity()
intensity /= np.max(intensity)
field.plot_intensity(intensity)

field.propagate(100 * mm)
# Define the first lens
focal_length_2 = 70 * mm  # Focal length of the first lens
lens2 = Lens(f=focal_length_2, radius= 10*beam_waist)
field.add(lens2)

field.propagate(200*mm)
gif_image = []
for i in range(0,140):
    field.propagate(0.5 * mm)
    intensity = field.get_intensity()
    intensity = intensity[256:768,256:768]
    intensity /= np.max(intensity)
    # field.plot_intensity(intensity)
    plt.imshow(intensity,extent=(x.min()/mm, x.max()/mm, y.min()/mm, y.max()/mm),cmap="inferno")
    plt.colorbar()
    plt.title(f"Intensity pattern on screen ({0.5*i+150} mm)")
    if(savegif==True):
        filename = 'diffraction_pattern.png'
        plt.savefig(filename)
        gif_image.append(imageio.imread(filename))
    plt.show()
    
    print(f"Progres: {i*100/140} %")
    

# Create GIF from images
if savegif==True:
    imageio.mimsave('D:\\USAF_imaging.gif', gif_image, duration=0.2)


__del_vars__ = []
# Print all variable names in the current local scope
print("Deleted Variables:")
for __var__ in dir():
    if not __var__.startswith("_") and not callable(locals()[__var__]) and not isinstance(locals()[__var__], types.ModuleType):
        __del_vars__.append(__var__)
        exec("del "+ __var__)
    del __var__
    
print(__del_vars__)