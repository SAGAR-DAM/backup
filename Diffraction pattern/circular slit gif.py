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

# Define the circular hole grating parameters
hole_radius = 50 * um  # Radius of each circular hole along x-axis
num_holes_x = 1  # Number of holes along x-axis
num_holes_y = 1  # Number of holes along y-axis
grid_period_x = 400 * um  # Spacing between holes along x-axis
grid_period_y = 200 * um  # Spacing between holes along y-axis

# Define the circular hole function
def circular_hole_grating(x, y, wavelength):
    hole_pattern = np.zeros_like(x)
    for i in range(num_holes_x):
        for j in range(num_holes_y):
            hole_center_x = (i - (num_holes_x - 1) / 2) * grid_period_x
            hole_center_y = (j - (num_holes_y - 1) / 2) * grid_period_y
            distance_from_center = np.sqrt((x - hole_center_x) ** 2 + (y - hole_center_y) ** 2)
            hole_pattern += np.where(distance_from_center < hole_radius, 1, 0)
    return hole_pattern


# Define function to generate diffraction pattern for a given distance
def generate_diffraction_pattern(distance):
    field = MonochromaticField(
        wavelength=wavelength,
        extent_x=5 * mm,
        extent_y=5 * mm,
        Nx=2000,
        Ny=2000
    )
    aperture = ApertureFromFunction(circular_hole_grating)
    field.add(aperture)
    field.propagate(distance * cm)
    intensity = field.get_intensity()
    return intensity

# Define distances
distances = np.linspace(0, 500, 101)  # From 1 mm to 100 mm in 20 steps

field = MonochromaticField(
    wavelength=wavelength,
    extent_x=5 * mm,
    extent_y=5 * mm,
    Nx=2000,
    Ny=2000
)
# Add the slit grating aperture to the field
aperture = ApertureFromFunction(circular_hole_grating)
field.add(aperture)
# Create the aperture pattern
x = field.xx
y = field.yy
aperture_pattern = circular_hole_grating(x, y, wavelength)

# Plot the aperture pattern
plt.figure()
plt.imshow(aperture_pattern, extent=(x.min()/mm, x.max()/mm, y.min()/mm, y.max()/mm), cmap='gray')
plt.title('Aperture Pattern')
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.colorbar(label='Transmittance')
plt.show()

# Generate diffraction patterns for each distance and save as images
images = []
for i, distance in enumerate(distances):
    intensity = generate_diffraction_pattern(distance)
    plt.imshow(intensity, extent=(x.min()/mm, x.max()/mm, y.min()/mm, y.max()/mm), cmap='inferno')
    plt.title(f'Distance: {distance} cm')
    plt.xlabel('x (mm)')
    plt.ylabel('y (mm)')
    plt.colorbar(label='Intensity')
    filename = 'diffraction_pattern.png'
    plt.savefig(filename)
    images.append(imageio.imread(filename))
    print(f"process: {i/len(distances)*100} %")
    plt.close()

# Create GIF from images
imageio.mimsave('D:\\diffraction_pattern_circ.gif', images, duration = 0.4)
