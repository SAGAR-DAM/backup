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
wavelength = 800 * nm  # 500 nm (green light)

# Define the slit grating parameters
slit_width = 100 * um  # Width of each slit
grating_period = 1000 * um  # Distance between the centers of adjacent slits
num_slits = 3  # Number of slits

# Define the slit function
def slit_grating(x, y, wavelength):
    slit_pattern = np.zeros_like(x)
    for i in range(num_slits):
        slit_center = (i - (num_slits - 1) / 2) * grating_period
        slit_pattern += np.where(np.abs(x - slit_center) < slit_width / 2, 1, 0)
    return slit_pattern

@np.vectorize
def get_phase(E):
    phase = (np.log(E)).imag
    return phase


# Create a monochromatic field
field = MonochromaticField(
    wavelength=wavelength,
    extent_x=5 * mm,
    extent_y=5 * mm,
    Nx=10000,
    Ny=100
)

# Add the slit grating aperture to the field
aperture = ApertureFromFunction(slit_grating)
field.add(aperture)

# Propagate the field to a certain distance
field.propagate(2 * cm)


# Create the aperture pattern
x = field.xx
y = field.yy
aperture_pattern = slit_grating(x, y, wavelength)

# Plot the aperture pattern
plt.figure()
plt.imshow(aperture_pattern, extent=(x.min()/mm, x.max()/mm, y.min()/mm, y.max()/mm), cmap='gray')
plt.title('Aperture Pattern')
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.colorbar(label='Transmittance')
plt.show()


# Compute the intensity of the propagated field
intensity = field.get_intensity()
intensity /= np.max(intensity)

# Visualize the field intensity
field.plot_intensity(intensity)


I_line = intensity[3,:]
plt.plot(field.xx[0,:]/mm,I_line,'r-',lw=0.5)
plt.title("Intenasity variation across screen")
plt.xlabel("x (mm)")
plt.ylabel(r"I$_{norm}$   (Arb unit)")
plt.show()


phase = get_phase(field.E)
plt.imshow(phase,extent=(x.min()/mm, x.max()/mm, y.min()/mm, y.max()/mm),cmap="jet")
plt.title("Phase pattern on screen")
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.colorbar(label='phase (rad)')
plt.show()