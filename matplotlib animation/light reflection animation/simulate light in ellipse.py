# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 17:48:47 2023

@author: mrsag
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

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

def simulate(ellipse_radii, light_source, angle, num_reflect):
    angle = angle*np.pi/180 - np.pi

    # Calculate the initial direction of the ray
    direction = np.array([np.cos(angle), np.sin(angle)])

    # Calculate the reflection of the ray
    intersection, reflected_direction = reflect(light_source, direction, np.array([0, 0]), ellipse_radii)
    points_x, points_y = [light_source[0],intersection[0]], [light_source[1],intersection[1]]

    # Simulate multiple reflections
    for _ in range(num_reflect):  # Change this to simulate more or fewer reflections
        # Calculate the next reflection
        new_intersection, new_reflected_direction = reflect(intersection, reflected_direction, np.array([0, 0]), ellipse_radii)

        # Update the intersection and direction for the next reflection
        intersection, reflected_direction = new_intersection, new_reflected_direction
        
        points_x.append(intersection[0])
        points_y.append(intersection[1])
    
    return(points_x, points_y)


def run_simulation_ellipse(ellipse_radii, light_source, angle, num_reflect,animsave):
    points_x,points_y=simulate(ellipse_radii, light_source, angle, num_reflect)
    print(f"ellipticity: {180*np.arctan(ellipse_radii[1]/ellipse_radii[0])/np.pi}")
    # Create a figure and axis
    fig, ax = plt.subplots()
    line, = ax.plot([], [], 'r-', lw = 0.5)
    plot_source, = ax.plot(light_source[0], light_source[1], 'o', markersize=2, color='yellow', label="source point")
    plot_focus, = ax.plot([np.sqrt(ellipse_radii[0]**2-ellipse_radii[1]**2),-np.sqrt(ellipse_radii[0]**2-ellipse_radii[1]**2)],[0,0],'x', markersize=2, color='cyan', label="focus")
    
    ellipse_scale_factor=1.01
    ellipse = patches.Ellipse((0, 0), 2*ellipse_radii[0]*ellipse_scale_factor, 2*ellipse_radii[1]*ellipse_scale_factor, edgecolor='w', facecolor='black',  linewidth=1.5)
    ax.add_patch(ellipse)
    ax.set_facecolor("black")
    ax.axis("equal")
    ax.tick_params(labelsize=5)  # Adjust the font size as needed
    ax.tick_params(labelsize=5)  # Adjust the font size as needed
    ax.legend(facecolor="black",labelcolor="white", fontsize=5)

    # Animation function
    def update(frame):
        if frame < len(points_x):
            line.set_data(points_x[:frame+1], points_y[:frame+1])
        plot_source.set_data(light_source[0], light_source[1])
        plot_focus.set_data([np.sqrt(ellipse_radii[0]**2-ellipse_radii[1]**2),-np.sqrt(ellipse_radii[0]**2-ellipse_radii[1]**2)],[0,0])
        return line, plot_source, plot_focus

    # Create animation
    # Set the frame rate to 30 frames per second
    frame_rate = 30
    interval = 1000 / frame_rate  # Calculate interval in milliseconds
    animation = FuncAnimation(fig, update, frames=len(points_x)+1, interval=interval, blit=True)
    
    if (animsave==True):
        animation.save('D:\\Codes\\matplotlib animation\\ellipse animation 2.gif', writer='pillow')

    # Show the plot
    plt.show()
    
    
# Define the room and light source
ellipse_radii = np.array([10,7.5])  # Radii of the ellipse
light_source = np.array([np.sqrt(ellipse_radii[0]**2-ellipse_radii[1]**2)-2.1,5])  # Position of the light source
angle = 20
num_reflect = 200
animsave = False


run_simulation_ellipse(ellipse_radii, light_source, angle, num_reflect, animsave)
