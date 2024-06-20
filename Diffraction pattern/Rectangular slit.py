from diffractsim import MonochromaticField, ApertureFromFunction, mm, cm, nm, um
import numpy as np
import matplotlib.pyplot as plt

import matplotlib as mpl

mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Times New Roman'
mpl.rcParams['font.size'] = 12
#mpl.rcParams['font.weight'] = 'bold'
#mpl.rcParams['font.style'] = 'italic'  # Set this to 'italic'
mpl.rcParams['figure.dpi'] = 300  # highres display

# Define the wavelength of the light
wavelength = 500 * nm  # 500 nm (green light)

# Define the square hole grating parameters
hole_side_length_x = 100 * um  # Side length of each square hole along x-axis
hole_side_length_y = 100 * um   # Side length of each square hole along y-axis
num_holes_x = 30  # Number of holes along x-axis
num_holes_y = 30  # Number of holes along y-axis
grid_period_x = 200 * um  # Spacing between holes along x-axis
grid_period_y = 200 * um  # Spacing between holes along y-axis

# Define the square hole function
def square_hole_grating(x, y, wavelength):
    hole_pattern = np.zeros_like(x)
    for i in range(num_holes_x):
        for j in range(num_holes_y):
            hole_center_x = (i - (num_holes_x - 1) / 2) * grid_period_x
            hole_center_y = (j - (num_holes_y - 1) / 2) * grid_period_y
            x_in_hole = np.abs(x - hole_center_x) < hole_side_length_x / 2
            y_in_hole = np.abs(y - hole_center_y) < hole_side_length_y / 2
            hole_pattern += np.where(x_in_hole & y_in_hole, 1, 0)
    return hole_pattern

# Create a monochromatic field
field = MonochromaticField(
    wavelength=wavelength,
    extent_x=5 * mm,
    extent_y=5 * mm,
    Nx=1000,
    Ny=1000
)

# Create the aperture pattern
x = field.xx
y = field.yy
aperture_pattern = square_hole_grating(x, y, wavelength)

# Plot the aperture pattern
plt.figure()
plt.imshow(aperture_pattern, extent=(x.min()/mm, x.max()/mm, y.min()/mm, y.max()/mm), cmap='gray')
plt.title('Aperture Pattern (Square Holes)')
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.colorbar(label='Transmittance')
plt.show()

# Add the square hole grating aperture to the field
aperture = ApertureFromFunction(square_hole_grating)
field.add(aperture)

# Propagate the field to a certain distance
field.propagate(5 * cm)

# Compute the intensity of the propagated field
intensity = field.get_intensity()

# Plot the intensity pattern
plt.figure()
plt.imshow(intensity, extent=(x.min()/mm, x.max()/mm, y.min()/mm, y.max()/mm), cmap='inferno')
plt.title('Diffraction Pattern')
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.colorbar(label='Intensity')
plt.show()
