"""
File: format.py
Author: Emily Cordero

Purpose: Write a program to practice formating strings.

"""
# Using format strings
car_count = 2
cars = 3
people = 8

# print(f'There are {car_count} cars on the road.')
print('There are {} cars on the road.'.format(car_count))

print()

# Defining the # of decimals to display
people_per_car = people / cars
print(f'There are {people_per_car:.1f} people in each car.\n')

print(f'There are {people_per_car:.2f} people in each car.\n')

print(f'There are {people_per_car:.3f} people in each car.\n')

# Scientific notation
distance = 9 * 1205 * 18

# Scientific notation with 3 digits of precision
print(f'The distance is: {distance:.3e} meters.\n')

# Scientific notation with 6 digits of precision
print(f'The distance is: {distance:.6e} meters.\n')

# Thousands grouping
big_number = 123456789

print(f'The number is: {big_number}\n')

# With "," formatting
print(f'The number is: {big_number:,}\n')

# With "_" formatting
print(f'The number is: {big_number:_}\n')

# Math library

import math
weight = 1.65

# math.ceil(value)rounds the value up to the next whole number, ceil for "ceiling"
higher = math.ceil(weight)
print(higher)
print()

# math.floor(value) rounds the value down to the next whole number, floor, for lower
lower = math.floor(weight)
print(lower)
print()

# math.exp(value) raises e to the power of the value
raised_exp = math.exp(weight)
print(raised_exp)
print()

# math.sin(value) computes the trigonometry sine function of value in radians
trig = math.sin(weight)
print(trig)
print()

