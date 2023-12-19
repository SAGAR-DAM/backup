# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 18:50:34 2023

@author: sagar
"""

import sys
import pygame
import math

# Pygame initialization
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Triple Pendulum Animation")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Pendulum parameters
pivot = (width // 2, 300)
pendulum1_length = 100
pendulum2_length = 100
pendulum3_length = 100
angle1 = math.pi/6
angle2 = -math.pi/3
angle3 = math.pi/4 
angular_velocity1 = 0.0
angular_velocity2 = 0.0
angular_velocity3 = 0.0

# Simulation settings
gravity = 500
time_step = 0.01

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate new positions of the pendulums
    num1 = -gravity * (3 * math.sin(angle1) + math.sin(angle1 - 2 * angle2) + 0.5 * math.sin(angle1 - 3 * angle2))
    num2 = 2 * math.sin(angle1 - angle2)
    num3 = angular_velocity1**2 * pendulum1_length + angular_velocity2**2 * pendulum2_length * math.cos(angle1 - angle2)
    den = pendulum1_length * (3 - math.cos(2 * angle1 - 2 * angle2))
    angular_acceleration1 = (num1 + num2 * num3) / den

    num1 = 2 * math.sin(angle1 - angle2)
    num2 = (angular_velocity1**2 * pendulum1_length * (2 * pendulum1_length + pendulum2_length - pendulum2_length * math.cos(angle1 - angle2))
            + angular_velocity2**2 * pendulum2_length**2 * math.sin(angle1 - angle2))
    den = pendulum2_length * (2 * pendulum1_length + pendulum2_length - pendulum2_length * math.cos(angle1 - angle2))
    angular_acceleration2 = (num1 * num2) / den

    num1 = 0.5 * math.sin(angle1 - 2 * angle2) * (angular_velocity1**2 * pendulum1_length * (2 * pendulum1_length + pendulum2_length)
                                                  + angular_velocity2**2 * pendulum2_length**2)
    num2 = 0.5 * math.sin(2 * (angle1 - angle2)) * angular_velocity1**2 * pendulum1_length * pendulum2_length
    den = pendulum2_length * (2 * pendulum1_length + pendulum2_length - pendulum2_length * math.cos(angle1 - angle2))
    angular_acceleration3 = (num1 + num2) / den

    angular_velocity1 += angular_acceleration1 * time_step
    angular_velocity2 += angular_acceleration2 * time_step
    angular_velocity3 += angular_acceleration3 * time_step
    angle1 += angular_velocity1 * time_step
    angle2 += angular_velocity2 * time_step
    angle3 += angular_velocity3 * time_step

    # Clear the screen
    screen.fill(black)

    # Draw the pendulums
    pendulum1_x = pivot[0] + pendulum1_length * math.sin(angle1)
    pendulum1_y = pivot[1] + pendulum1_length * math.cos(angle1)
    pendulum2_x = pendulum1_x + pendulum2_length * math.sin(angle2)
    pendulum2_y = pendulum1_y + pendulum2_length * math.cos(angle2)
    pendulum3_x = pendulum2_x + pendulum3_length * math.sin(angle3)
    pendulum3_y = pendulum2_y + pendulum3_length * math.cos(angle3)

    pygame.draw.line(screen, white, pivot, (pendulum1_x, pendulum1_y), 1)
    pygame.draw.line(screen, white, (pendulum1_x, pendulum1_y), (pendulum2_x, pendulum2_y), 1)
    pygame.draw.line(screen, white, (pendulum2_x, pendulum2_y), (pendulum3_x, pendulum3_y), 1)
    pygame.draw.circle(screen, red, (int(pendulum1_x), int(pendulum1_y)), 10)
    pygame.draw.circle(screen, red, (int(pendulum2_x), int(pendulum2_y)), 10)
    pygame.draw.circle(screen, red, (int(pendulum3_x), int(pendulum3_y)), 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
