"""
File: speed_team.py
Author: Emily Cordero

Purpose: Write a program with team that calculates the speed of a falling object. 

"""

# Import math library
import math

# Welcoming statement
print('Welcome to the velocity calculator. Please enter the following: ')

# Stretch challenge #1
# I choose a bowling ball

# Ask user for mass in kg (m)
mass_in_kg = float(input('Mass (in kg): '))

# Ask user for gravity for Jupiter and Earth (g)
gravity_in_ms = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))

# Ask user for time in seconds (t)
time_in_seconds = float(input('Time (in seconds): '))

# Ask user for density of the fluid (p)
density_of_fluid = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))

# Ask user for cross sectional area of a bowling ball and its radius (A)
# cross_sectional_area = float(input('Cross sectional area (in m^2): '))
radius_for_ball = float(input('Radius for bowling ball: '))

cross_sectional_area_for_bowling_ball = math.pi * (radius_for_ball ** 2)

# Ask user for drag constant (C)
drag_constant = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

print()

# Print the value of C
# c = ( 1 / 2) * p * A * C
c = (1/2) * density_of_fluid * cross_sectional_area_for_bowling_ball * drag_constant

print(f'The inner value of c is: {c:.3f}')

# Print the value of velocity
# v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))
velocity_for_earth = math.sqrt((mass_in_kg * gravity_in_ms) / c) * (1 - math.exp((-math.sqrt(mass_in_kg * gravity_in_ms * c)/mass_in_kg)* time_in_seconds))

# Stretch 2- velocity fir Jupiter
velocity_for_jupiter = math.sqrt((mass_in_kg * 24) / c) * (1 - math.exp((-math.sqrt(mass_in_kg * 24 * c)/mass_in_kg)* time_in_seconds))

print(f'The velocity for Earth m/s after {time_in_seconds} is: {velocity_for_earth:.3f} m/s')

# Print velocity of Jupiter and compare to Earth's
print(f'The velocity for Jupiter m/s after {time_in_seconds} is: {velocity_for_jupiter:.3f} m/s')

difference_velocities = velocity_for_jupiter - velocity_for_earth
print(f'The difference of Jupiter and Earch is by {difference_velocities:.3f} m/s')

# Stretch 3 determine v_terminal
# v_terminal (sqrt(mg/c))
v_terminal = math.sqrt((mass_in_kg * gravity_in_ms)/c)
print(f'The terminal velocity is: {v_terminal:.3f} m/s')

