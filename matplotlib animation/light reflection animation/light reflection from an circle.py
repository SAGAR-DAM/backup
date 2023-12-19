# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 10:23:56 2023

@author: sagar
"""

import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams['figure.dpi']=300 # highres display


def reflect(ray_origin, ray_direction, circle_center, circle_radius):
    # Calculate the intersection of the ray with the circle
    oc = ray_origin - circle_center
    a = np.dot(ray_direction, ray_direction)
    b = 2 * np.dot(oc, ray_direction)
    c = np.dot(oc, oc) - circle_radius**2
    discriminant = b**2 - 4*a*c
    t = (-b - np.sqrt(discriminant)) / (2*a)
    intersection = ray_origin + t * ray_direction

    # Calculate the normal at the intersection
    normal = (intersection - circle_center) / np.linalg.norm(intersection - circle_center)

    # Calculate the reflected direction
    reflected_direction = ray_direction - 2 * np.dot(ray_direction, normal) * normal

    return intersection, reflected_direction

# Define the room and light source
room_radius = 10
light_source = np.array([0, 9])  # Position of the light source
num_rays = 7  # Number of light rays
num_reflect = 60

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Draw the room (circle with radius=room_radius)
circle_scale_factor=1.01
circle = plt.Circle((0, 0), room_radius*circle_scale_factor, edgecolor='w', facecolor='none',linewidth=2.5)
ax.add_artist(circle)


# Calculate the angles for the light rays
angles = np.arange(0, 2*np.pi, (2*np.pi/num_rays))
angles = angles - np.pi

# For each angle...
for angle in angles:
    # Calculate the initial direction of the ray
    direction = np.array([np.cos(angle), np.sin(angle)])

    # Calculate the reflection of the ray
    intersection, reflected_direction = reflect(light_source, direction, np.array([0, 0]), room_radius)

    # Draw the initial ray
    ax.plot([light_source[0], intersection[0]], [light_source[1], intersection[1]], 'r-',lw=0.5)

    # Simulate multiple reflections
    for _ in range(num_reflect):  # Change this to simulate more or fewer reflections
        # Calculate the next reflection
        new_intersection, new_reflected_direction = reflect(intersection, reflected_direction, np.array([0, 0]), room_radius)

        # Draw the reflected ray
        ax.plot([intersection[0], new_intersection[0]], [intersection[1], new_intersection[1]], 'r-', lw=0.5)

        # Update the intersection and direction for the next reflection
        intersection, reflected_direction = new_intersection, new_reflected_direction

# Set the same scale for both axes and enable the grid

ax.plot(light_source[0], light_source[1], 'o', markersize=5, color='yellow', label="source point")
ax.axis("equal")
ax.grid(False)
ax.plot([0,0],[0,0],'x', markersize=5, color='cyan', label="centre")
ax.legend(facecolor="black",labelcolor="white")
ax.set_facecolor('black')

# Show the plot
plt.show()