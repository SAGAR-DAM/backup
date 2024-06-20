from diffractsim import MonochromaticField, ApertureFromFunction, mm, cm, nm, um
import numpy as np
import matplotlib.pyplot as plt
import imageio


import matplotlib as mpl

mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Times New Roman'
mpl.rcParams['font.size'] = 12
#mpl.rcParams['font.weight'] = 'bold'
#mpl.rcParams['font.style'] = 'italic'  # Set this to 'italic'
mpl.rcParams['figure.dpi'] = 300  # highres display


# Define the wavelength of the light
wavelength = 500 * nm  # 500 nm (green light)

# Define the slit grating parameters
slit_width = 10 * um  # Width of each slit
grid_period = 40 * um  # Distance between the centers of adjacent slits
num_slits = 20  # Number of slits

# Define the slit function
def slit_grating(x, y, wavelength):
    slit_pattern = np.zeros_like(x)
    for i in range(num_slits):
        slit_center = (i - (num_slits - 1) / 2) * grid_period
        slit_pattern += np.where(np.abs(x - slit_center) < slit_width / 2, 1, 0)
    return slit_pattern

# Define function to generate diffraction pattern for a given distance
def generate_diffraction_pattern(distance):
    field = MonochromaticField(
        wavelength=wavelength,
        extent_x=15 * mm,
        extent_y=15 * mm,
        Nx=1000,
        Ny=1000
    )
    aperture = ApertureFromFunction(slit_grating)
    field.add(aperture)
    field.propagate(distance * cm)
    intensity = field.get_intensity()
    return intensity

# Define distances
distances = np.arange(1, 401, 3)  # From 1 mm to 100 mm in 20 steps

field = MonochromaticField(
    wavelength=wavelength,
    extent_x=15 * mm,
    extent_y=15 * mm,
    Nx=1000,
    Ny=1000
)
# Add the slit grating aperture to the field
aperture = ApertureFromFunction(slit_grating)
field.add(aperture)
# Create the aperture pattern
x = field.xx
y = field.yy
aperture_pattern = slit_grating(x, y, wavelength)

# Plot the aperture pattern
plt.figure()
plt.imshow(aperture_pattern, extent=(x.min(), x.max(), y.min(), y.max()), cmap='gray')
plt.title('Aperture Pattern')
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.colorbar(label='Transmittance')
plt.show()

# Generate diffraction patterns for each distance and save as images
images = []
for i, distance in enumerate(distances):
    intensity = generate_diffraction_pattern(distance)
    plt.imshow(intensity, extent=(x.min(), x.max(), y.min(), y.max()), cmap='inferno')
    plt.title(f'Distance: {int(distance)} cm')
    plt.xlabel('x (mm)')
    plt.ylabel('y (mm)')
    plt.colorbar(label='Intensity')
    filename = 'diffraction_pattern.png'
    plt.savefig(filename)
    images.append(imageio.imread(filename))
    print(f"process: {i/len(distances)*100} %")
    plt.close()

# Create GIF from images
imageio.mimsave('D:\\diffraction_pattern.gif', images)
