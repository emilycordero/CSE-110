"""
File: shapes.py
Author: Emily Cordero

Purpose: Write a program to compute the areas of three different shapes.

"""
# Import math library for the stretch 1
import math
 
# Length of a side of a square
square_length = float(input('What is the length of a side of the square? '))
print(f'The area of the square is: {float(square_length ** 2)}')

# Length of a rectangle
rectangle_length = float(input('What is the length of a rectangle? '))
rectangle_width = float(input('What is the width of a rectangle? '))
print(f'The area of the rectangle is: {float(rectangle_length * rectangle_width)}')

# Radius of a circle - I use the math library and math.pi for the Stretch 1
radius_circle = float(input('What is the radius of a circle? '))
radius_sq = float(radius_circle ** 2)
print(f'The area of a circle: {float(math.pi * (radius_sq))}')

# Part 2 stretch challenge
# Ask user for one value
single_value = float(input('Please give us a value to be used: '))

# Calculations for area/volume of a square and circle/cube and a sphere
area_square = single_value ** 2
area_circle = math.pi * area_square
volume_of_cube = single_value ** 3
volume_of_sphere = (4/3) * math.pi * (volume_of_cube)

# Displaying the results
print(f'Area of square: {area_square}')
print(f'Area of circle: {area_circle}')
print(f'Volume of cube: {volume_of_cube}')
print(f'Volume of sphere: {volume_of_sphere}')

# Part 3 stretch challenge 
# Converting  cm to m for a square
side_of_square = float(input('What is the side of the square in Centimeters? '))
area_square = side_of_square ** 2
print(f'The area of the square in cm^2 is: {area_square}')
print(f'The area of the square in m^2 is: {area_square/10000}')

# Converting cm to m for a rectangle
rectangle_length_in_cm = float(input('What is the length of a rectangle in Centimeters? '))
rectangle_width_in_cm = float(input('What is the width of a rectangle in Centimeters? '))
area_of_rectangle = rectangle_length_in_cm * rectangle_width_in_cm
print(f'The area of a rectangle in cm^2 is: {area_of_rectangle}')
print(f'The area of a rectangle in m^2 is: {area_of_rectangle/10000}')

# Converting to cm to m for a circle
radius_of_circle_in_cm = float(input("What is the radius of the circle in cm^2? "))
area_circle = math.pi * (radius_of_circle_in_cm **2)
print(f'The area of the circle in cm^2 is: {area_circle}')
print(f'The area of the circle in m^2 is: {area_circle / 10000}')

