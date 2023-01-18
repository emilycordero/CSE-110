"""
File: team.py
Author: Emily Cordero

Purpose: Write a program to compute the areas of three different shapes as a team.

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
# single_value = float(input('Please give us the value for a '))
# print(f'(The area of your square is: {single_value ** 2}')
# value_squared = float(single_value **2)
# print(f'The area of your circle: {float(value_squared) * math.pi}')
# print(f'The area of your cube is: {value_squared * 6}')
# print(f'The area of the sphere: {value_squared * math.pi *4}')

# Part 3 stretch challenge 
circ_radius = float(input('What is the radius of a circle in Centimeters? '))
print(f'The area of the circle is {(circ_radius ** 2) * math.pi} sq.cm')
print(f'The area of the circle is {((circ_radius ** 2) * math.pi)/1000} sq.m')