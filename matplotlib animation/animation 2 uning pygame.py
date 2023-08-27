# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 11:14:46 2023

@author: sagar
"""

import pygame
import numpy as np

# Parameters
G = 9.81  # acceleration due to gravity (m/s^2)
L1 = 200  # length of the first pendulum (pixels)
L2 = 100  # length of the second pendulum (pixels)
M1 = 20   # mass of the first pendulum (arbitrary units)
M2 = 20   # mass of the second pendulum (arbitrary units)

# Initialize Pygame
pygame.init()

# Screen parameters
width, height = 800, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Double Pendulum Simulation")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red= (255,0,0)

# Initial conditions
theta1 = np.pi / 1  # initial angle of the first pendulum (rad)
theta2 = np.pi / 2  # initial angle of the second pendulum (rad)

omega1 = 0.1        # initial angular velocity of the first pendulum (rad/s)
omega2 = 0.0        # initial angular velocity of the second pendulum (rad/s)

# Time parameters
dt = 0.005  # time step (s)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update angles and angular velocities
    alpha1_num = -G * (2 * M1 + M2) * np.sin(theta1) - M2 * G * np.sin(theta1 - 2 * theta2) - 2 * np.sin(theta1 - theta2) * M2 * (omega2 ** 2 * L2 + omega1 ** 2 * L1 * np.cos(theta1 - theta2))
    alpha1_den = L1 * (2 * M1 + M2 - M2 * np.cos(2 * theta1 - 2 * theta2))
    alpha2_num = 2 * np.sin(theta1 - theta2) * (omega1 ** 2 * L1 * (M1 + M2) + G * (M1 + M2) * np.cos(theta1) + omega2 ** 2 * L2 * M2 * np.cos(theta1 - theta2))
    alpha2_den = L2 * (2 * M1 + M2 - M2 * np.cos(2 * theta1 - 2 * theta2))

    alpha1 = alpha1_num / alpha1_den
    alpha2 = alpha2_num / alpha2_den

    omega1 += alpha1 * dt
    omega2 += alpha2 * dt
    theta1 += omega1 * dt
    theta2 += omega2 * dt

    # Calculate pendulum positions
    x1 = int(width / 2 + L1 * np.sin(theta1))
    y1 = int(height / 2 + L1 * np.cos(theta1))
    x2 = int(x1 + L2 * np.sin(theta2))
    y2 = int(y1 + L2 * np.cos(theta2))

    # Draw pendulum
    screen.fill(black)
    pygame.draw.line(screen, white, (width // 2, height // 2), (x1, y1), 5)
    pygame.draw.line(screen, red, (x1, y1), (x2, y2), 5)
    pygame.draw.circle(screen, white, (x1, y1), 10)
    pygame.draw.circle(screen, red, (x2, y2), 10)
    pygame.display.flip()

pygame.quit()
