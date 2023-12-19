
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:57:27 2023

@author: mrsag
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math 

import matplotlib
matplotlib.rcParams["figure.dpi"]=200

r=30
polygon_scale=1.015

def regular_polygon(sides):
    # Center of the polygon
    center = (0, 0)

    # Radius of the circle circumscribing the polygon
    radius = 10.0

    # Calculate angles for each vertex
    angles = np.linspace(0, 2 * np.pi, sides, endpoint=False)

    # Calculate coordinates of vertices
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    
    x = np.append(x,x[0])
    y = np.append(y,y[0])
    return x,y

def calculate_angle(a, b, c):
    # Calculate vectors AB and BC
    ab = [b[0] - a[0], b[1] - a[1]]
    bc = [c[0] - b[0], c[1] - b[1]]

    # Calculate angles of vectors AB and BC
    angle_ab = math.atan2(ab[1], ab[0])
    angle_bc = math.atan2(bc[1], bc[0])

    # Calculate the angle between vectors in the specified order
    angle_abc = angle_bc - angle_ab

    # Convert angle to degrees
    angle_degrees = (math.pi-angle_abc)
    if(angle_degrees <= np.pi):
        return angle_degrees
    else:
        return(angle_degrees-2*np.pi)
    
def is_point_on_line(point1, point2, check_point):
    x1, y1 = point1
    x2, y2 = point2
    x, y = check_point

    # Check if the slopes of (point1, point2) and (point1, check_point) are equal
    return (y2 - y1) * (x - x1) == (y - y1) * (x2 - x1)
    
def on_same_side(p1, p2, line_point1, line_point2):
    # Calculate vectors
    vec_line = [line_point2[0] - line_point1[0], line_point2[1] - line_point1[1]]
    vec_p1 = [p1[0] - line_point1[0], p1[1] - line_point1[1]]
    vec_p2 = [p2[0] - line_point1[0], p2[1] - line_point1[1]]

    # Calculate cross products
    cross_product_p1 = vec_line[0] * vec_p1[1] - vec_line[1] * vec_p1[0]
    cross_product_p2 = vec_line[0] * vec_p2[1] - vec_line[1] * vec_p2[0]

    # Check if cross products have the same sign
    return (cross_product_p1 >= 0 and cross_product_p2 >= 0) or (cross_product_p1 < 0 and cross_product_p2 < 0)


def find_vertices_of_reflecting_wall(second_point,source,poly_x,poly_y):
    for i in range(len(poly_x)-1):
        a=second_point
        b=source
        c1=[poly_x[i],poly_y[i]]
        c2=[poly_x[i+1],poly_y[i+1]]
        
        angle_1=calculate_angle(a, b, c1)
        angle_2=calculate_angle(a, b, c2)
        if(angle_1*angle_2<0 and abs(angle_1)<=np.pi/2 and abs(angle_2)<=np.pi/2 and not(is_point_on_line(point1=c1, point2=c2, check_point=source))):
            break
        
    return c1,c2

def find_vertices_of_reflecting_wall_exception(second_point,source,poly_x,poly_y):
    for i in range(len(poly_x)-1):
        a=second_point
        b=source
        c1=[poly_x[i],poly_y[i]]
        c2=[poly_x[i+1],poly_y[i+1]]
        
        if(not(on_same_side(p1=c1, p2=c2, line_point1=source, line_point2=second_point)) and not(is_point_on_line(point1=c1, point2=c2, check_point=source))):
            angle_1=calculate_angle(a, b, c1)
            angle_2=calculate_angle(a, b, c2)
            
            if(angle_1*angle_2<0):   
                break
    return c1,c2

def find_intersection(p1, p2, p3, p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    # Calculate slopes of the lines
    m1 = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else float('inf')
    m2 = (y4 - y3) / (x4 - x3) if x4 - x3 != 0 else float('inf')

    # Check if the lines are parallel
    if m1 == m2:
        print("Lines are parallel, no intersection.")
        return None
    # Calculate intersection point
    
    if(abs(p3[0]-p4[0])<1e-4):
        x_intersect = p3[0]
        y_intersect = m1 * (x_intersect - x1) + y1
    elif(abs(p3[1]-p4[1])<1e-4):
        y_intersect = p3[1]
        x_intersect = (m1 * x1 - m2 * x3 + y3 - y1) / (m1 - m2)
    else:
        x_intersect = (m1 * x1 - m2 * x3 + y3 - y1) / (m1 - m2)
        y_intersect = m1 * (x_intersect - x1) + y1

    return x_intersect, y_intersect

def next_point(source,angle,poly_x,poly_y):
    second_point = np.array([source[0]+r*np.cos(angle),source[1]+r*np.sin(angle)])

    c1,c2=find_vertices_of_reflecting_wall(second_point, source, poly_x, poly_y)

    if (on_same_side(p1=c1, p2=c2, line_point1=source, line_point2=second_point)==True):
        c1,c2=find_vertices_of_reflecting_wall_exception(second_point, source, poly_x, poly_y)

    new_source_x, new_source_y = find_intersection(p1=source, p2=second_point, p3=c1, p4=c2)
    new_source = np.array([new_source_x,new_source_y])
    
    incident_angle = np.pi/2-abs(calculate_angle(c2,new_source,source))
    
    theta0 = calculate_angle([-20,new_source[1]],new_source,source)
    
    new_angle = -(theta0)+2*incident_angle-np.pi
    
    return new_source,new_angle
    
    
def simulate_reflections(polygon_order, source, angle, num_reflect):
    
    poly_x,poly_y = regular_polygon(polygon_order)
    points_x = [source[0]]
    points_y = [source[1]]
    light_source=source
    
    for i in range(num_reflect):
        print(f"step:  {i}"+"\n_______________")
        print(f"source:  {source}")
        print(f"angle:   {np.degrees(angle)}")
        
        source,angle = next_point(source, angle, poly_x, poly_y)

        points_x.append(source[0])
        points_y.append(source[1])
        
    return(points_x,points_y)

def run_simulation_for_polygon(polygon_order, source, angle, num_reflect, animsave):
    points_x,points_y = simulate_reflections(polygon_order=polygon_order,source=source,angle=angle,num_reflect=num_reflect)

    poly_x,poly_y = regular_polygon(polygon_order)

    # Create a figure and axis
    fig, ax = plt.subplots()
    line, = ax.plot([], [], 'r-', lw = 0.5)
    plot_source, = ax.plot(source[0], source[1], 'o', markersize=5, color='yellow', label="source point")

    ax.plot(polygon_scale*poly_x,polygon_scale*poly_y,'w-',lw=2)
    ax.set_facecolor("black")
    ax.axis("equal")
    ax.tick_params(labelsize=8)  # Adjust the font size as needed
    ax.tick_params(labelsize=8)  # Adjust the font size as needed
    ax.legend(facecolor="black",labelcolor="white")

    # Animation function
    def update(frame):
        if frame < len(points_x):
            line.set_data(points_x[:frame+1], points_y[:frame+1])
        plot_source.set_data(source[0], source[1])
        return line, plot_source

    # Create animation
    # Set the frame rate to 30 frames per second
    frame_rate = 30
    interval = 1000 / frame_rate  # Calculate interval in milliseconds
    animation = FuncAnimation(fig, update, frames=len(points_x)+1, interval=interval, blit=True)
    
    if (animsave==True):
        animation.save('D:\\Codes\\matplotlib animation\\polygon animation 2.gif', writer='pillow')
    # Show the plot
    plt.show()
    

polygon_order = 6
source = [2,3]
angle = np.radians(45)
num_reflect = 200
animsave = False

run_simulation_for_polygon(polygon_order, source, angle, num_reflect, animsave)