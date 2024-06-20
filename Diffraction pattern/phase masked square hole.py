from diffractsim import MonochromaticField, ApertureFromFunction, mm, cm, nm, um
import numpy as np
import matplotlib.pyplot as plt
import types

import matplotlib as mpl

mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Times New Roman'
mpl.rcParams['font.size'] = 12
#mpl.rcParams['font.weight'] = 'bold'
#mpl.rcParams['font.style'] = 'italic'  # Set this to 'italic'
mpl.rcParams['figure.dpi'] = 300  # highres display

# Define the wavelength of the light
wavelength = 800 * nm  # 500 nm (green light)

# Define the square hole grating parameters
hole_side_length_x = 26 * um  # Side length of each square hole along x-axis
hole_side_length_y = 26 * um   # Side length of each square hole along y-axis
num_holes_x = 16  # Number of holes along x-axis
num_holes_y = 16  # Number of holes along y-axis
grid_period_x = 39 * um  # Spacing between holes along x-axis
grid_period_y = 39 * um  # Spacing between holes along y-axis

distance = 1   # in cm
phase_ret = 1*np.pi   # give the phase change on phase masked area...

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

def phase_plate_pattern(x, y):
    global phase_ret
    phase_pattern = np.zeros_like(x)  # Initialize with 1s
    for i in range(num_holes_x):
        for j in range(num_holes_y):
            hole_center_x = (i - (num_holes_x - 1) / 2) * grid_period_x
            hole_center_y = (j - (num_holes_y - 1) / 2) * grid_period_y
            x_in_hole = np.abs(x - hole_center_x) < hole_side_length_x / 2
            y_in_hole = np.abs(y - hole_center_y) < hole_side_length_y / 2
            if (i + j) % 2 == 0:  # Apply phase shift in a chessboard pattern
                phase_pattern += np.where(x_in_hole & y_in_hole, 1, 0)
    return phase_pattern

# Create a monochromatic field
field = MonochromaticField(
    wavelength=wavelength,
    extent_x=0.637 * mm,
    extent_y=0.637 * mm,
    Nx=1000,
    Ny=1000
)

# Create the aperture pattern
x = field.xx
y = field.yy
aperture_pattern = square_hole_grating(x, y, wavelength)
phase_plate = phase_plate_pattern(x, y)

# Plot the aperture pattern
plt.figure()
plt.imshow(aperture_pattern, extent=(x.min()/mm, x.max()/mm, y.min()/mm, y.max()/mm), cmap='gray')
plt.title('Aperture Pattern (square Holes)')
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
aperture = ApertureFromFunction(square_hole_grating)
    
# Add the aperture to the field
field.add(aperture)

# def make_phase_zero(field,x,y):
    
        

# Create a phase mask
def phase_mask(field, x, y):
    phase_added_field = field.E.astype(np.complex128)
    # Define the region where the phase is altered (e.g., left half of the aperture)
    mask_region = (phase_plate==1)#(x<0)
    phase_added_field[mask_region] *= np.exp(1j*phase_ret) #np.where(mask_region==1,np.exp(1j*np.pi),1)    
    return phase_added_field

@np.vectorize
def get_phase(E):
    phase = (np.log(E)).imag
    return phase


phase = get_phase(field.E)
plt.imshow(phase,extent=(x.min()/mm, x.max()/mm, y.min()/mm, y.max()/mm),cmap="jet")
plt.title("Phase pattern before aperture")
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.colorbar(label='phase (rad)')
plt.show()

# Apply the phase mask to the field
field.E = phase_mask(field, field.xx, field.yy)

phase = get_phase(field.E)
plt.imshow(phase,extent=(x.min()/mm, x.max()/mm, y.min()/mm, y.max()/mm),cmap="jet")
plt.title("Phase pattern on aperture")
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.colorbar(label='phase (rad)')
plt.show()


# Propagate the field to the observation screen
field.propagate(distance * cm)


phase = get_phase(field.E)
plt.imshow(phase,extent=(x.min()/mm, x.max()/mm, y.min()/mm, y.max()/mm),cmap="jet")
plt.title(f"Phase pattern on screen ({distance} cm)")
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.colorbar(label='phase (rad)')
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