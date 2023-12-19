# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 17:48:47 2023

@author: mrsag
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import matplotlib
matplotlib.rcParams['figure.dpi']=300 # highres display

def reflect(ray_origin, ray_direction, ellipse_center, ellipse_radii):
    # Transform the ray to the space of the unit circle
    transformed_origin = (ray_origin - ellipse_center) / ellipse_radii
    transformed_direction = ray_direction / ellipse_radii

    # Calculate the intersection of the transformed ray with the unit circle
    oc = transformed_origin
    a = np.dot(transformed_direction, transformed_direction)
    b = 2 * np.dot(oc, transformed_direction)
    c = np.dot(oc, oc) - 1
    discriminant = b**2 - 4*a*c
    t = (-b - np.sqrt(discriminant)) / (2*a)
    transformed_intersection = transformed_origin + t * transformed_direction

    # Transform the intersection back to the space of the ellipse
    intersection = transformed_intersection * ellipse_radii + ellipse_center

    # Calculate the normal at the intersection
    normal = (intersection - ellipse_center) / ellipse_radii**2
    normal /= np.linalg.norm(normal)

    # Calculate the reflected direction
    reflected_direction = ray_direction - 2 * np.dot(ray_direction, normal) * normal

    return intersection, reflected_direction

# Define the room and light source
ellipse_radii = np.array([10,7.5])  # Radii of the ellipse
light_source = np.array([np.sqrt(ellipse_radii[0]**2-ellipse_radii[1]**2)-2.1,0])  # Position of the light source
num_rays = 1  # Number of light rays
num_reflect = 200

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Draw the room (ellipse with given radii)
ellipse_scale_factor=1.01
ellipse = patches.Ellipse((0, 0), 2*ellipse_radii[0]*ellipse_scale_factor, 2*ellipse_radii[1]*ellipse_scale_factor, edgecolor='w', facecolor='black',  linewidth=2.5)
ax.add_patch(ellipse)

# Calculate the angle for the light rays
angle = 30
angle = angle*np.pi/180 - np.pi


# Calculate the initial direction of the ray
direction = np.array([np.cos(angle), np.sin(angle)])

# Calculate the reflection of the ray
intersection, reflected_direction = reflect(light_source, direction, np.array([0, 0]), ellipse_radii)

# Draw the initial ray
ax.plot([light_source[0], intersection[0]], [light_source[1], intersection[1]], 'r-', lw=0.5)

# Simulate multiple reflections
for _ in range(num_reflect):  # Change this to simulate more or fewer reflections
    # Calculate the next reflection
    new_intersection, new_reflected_direction = reflect(intersection, reflected_direction, np.array([0, 0]), ellipse_radii)

    # Draw the reflected ray
    ax.plot([intersection[0], new_intersection[0]], [intersection[1], new_intersection[1]], 'r-', lw=0.5)

    # Update the intersection and direction for the next reflection
    intersection, reflected_direction = new_intersection, new_reflected_direction

# Set the same scale for both axes and enable the grid
ax.plot(light_source[0], light_source[1], 'o', markersize=5, color='yellow', label="source point")
ax.plot([np.sqrt(ellipse_radii[0]**2-ellipse_radii[1]**2),-np.sqrt(ellipse_radii[0]**2-ellipse_radii[1]**2)],[0,0],'x', markersize=5, color='cyan', label="focus")
ax.legend(facecolor="black",labelcolor="white")
ax.axis('equal')
ax.grid(False)
ax.set_facecolor('black')


# Show the plot
plt.show()


print(f"ellipticity: {180*np.arctan(ellipse_radii[1]/ellipse_radii[0])/np.pi}")