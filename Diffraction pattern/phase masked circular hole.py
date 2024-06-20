import numpy as np
import matplotlib.pyplot as plt
from diffractsim import MonochromaticField, ApertureFromFunction, mm, cm, nm, um
import types 
import pyttsx3

import matplotlib as mpl

mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Times New Roman'
mpl.rcParams['font.size'] = 12
#mpl.rcParams['font.weight'] = 'bold'
#mpl.rcParams['font.style'] = 'italic'  # Set this to 'italic'
mpl.rcParams['figure.dpi'] = 300  # highres display

wavelength = 632 * nm


# Define the circular hole grating parameters
hole_radius = 50 * um  # Radius of each circular hole
num_holes_x = 15      # Number of holes along x-axis
num_holes_y = 15     # Number of holes along y-axis
grid_period_x = 100 * um  # Spacing between holes along x-axis
grid_period_y = 100 * um  # Spacing between holes along y-axis

distance = 10  #in cm
phase_ret = np.pi   # give the phase change on phase masked area...


# Initialize a monochromatic field
field = MonochromaticField(
    wavelength=wavelength,  # Wavelength of the incoming light
    extent_x=5.0 * mm,      # Extent of the field in the x direction
    extent_y=5.0 * mm,      # Extent of the field in the y direction
    Nx=1000,                # Number of points in the x direction
    Ny=1000                 # Number of points in the y direction
)

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


def phase_plate_pattern(x, y):
    phase_pattern = np.zeros_like(x)  # Initialize with 1s
    for i in range(num_holes_x):
        for j in range(num_holes_y):
            hole_center_x = (i - (num_holes_x - 1) / 2) * grid_period_x
            hole_center_y = (j - (num_holes_y - 1) / 2) * grid_period_y
            distance_from_center = np.sqrt((x - hole_center_x) ** 2 + (y - hole_center_y) ** 2)
            if (i + j) % 2 == 0:  # Apply phase shift in a chessboard pattern
                phase_pattern += np.where(distance_from_center < hole_radius, 1, 0)
    return phase_pattern

# Create the aperture pattern
x = field.xx
y = field.yy
aperture_pattern = circular_hole_grating(x, y, wavelength)
phase_plate = phase_plate_pattern(x, y)

# Plot the aperture pattern
plt.figure()
plt.imshow(aperture_pattern, extent=(x.min()/mm, x.max()/mm, y.min()/mm, y.max()/mm), cmap='gray')
plt.title('Aperture Pattern (Circular Holes)')
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.colorbar(label='Transmittance')
plt.show()

# Plot the aperture pattern
plt.figure()
plt.imshow(phase_plate, extent=(x.min()/mm, x.max()/mm, y.min()/mm, y.max()/mm), cmap='gray')
plt.title('phase plate Pattern')
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.colorbar(label='phase plate presence')
plt.show()

# Create an aperture from the function
aperture = ApertureFromFunction(circular_hole_grating)
    
# Add the aperture to the field
field.add(aperture)

# def make_phase_zero(field,x,y):
    
        

# Create a phase mask
def phase_mask(field, x, y):
    global phase_ret
    phase_added_field = field.E.astype(np.complex128)
    # Define the region where the phase is altered (e.g., left half of the aperture)
    mask_region = (phase_plate==1)#(x<0)
    phase_added_field[mask_region] *= np.exp(1j*phase_ret) #np.where(mask_region==1,np.exp(1j*np.pi),1)    
    return phase_added_field

@np.vectorize
def get_phase(E):
    phase = -(np.log(E)).imag
    return phase


phase = get_phase(field.E)
plt.imshow(phase,extent=(x.min()/mm, x.max()/mm, y.min()/mm, y.max()/mm),cmap="jet")
plt.colorbar()
plt.title("Phase pattern before aperture")
plt.show()

# Apply the phase mask to the field
field.E = phase_mask(field, field.xx, field.yy)

phase = get_phase(field.E)
plt.imshow(phase,extent=(x.min()/mm, x.max()/mm, y.min()/mm, y.max()/mm),cmap="jet")
plt.colorbar()
plt.title("Phase pattern on aperture")
plt.show()


# Propagate the field to the observation screen
field.propagate(distance * cm)


phase = get_phase(field.E)
plt.imshow(phase,extent=(x.min()/mm, x.max()/mm, y.min()/mm, y.max()/mm),cmap="jet")
plt.colorbar()
plt.title(f"Phase pattern on screen ({distance} cm)")
plt.show()


# Plot the intensity and phase of the resulting field
intensity = field.get_intensity()
intensity /= np.max(intensity)
field.plot_intensity(intensity)


__del_vars__ = []
# Print all variable names in the current local scope
print("Deleted Variables:")
for __var__ in dir():
    if not __var__.startswith("_") and not callable(locals()[__var__]) and not isinstance(locals()[__var__], types.ModuleType):
        __del_vars__.append(__var__)
        exec("del "+ __var__)
    del __var__
    
print(__del_vars__)

# engine = pyttsx3.init()
# engine.say("Hey your program has been completed!!")
# engine.runAndWait()

# del(engine)