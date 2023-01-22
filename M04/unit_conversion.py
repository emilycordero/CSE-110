"""
File: unit_conversion.py
Author: Emily Cordero

Purpose: Write a program to program to convert from Fahrenheit to Celsius. Display the result to one decimal place of precision.

"""

# Ask the user for temperature in Fahrenheit
temp_in_fahrenheit = float(input('What is the temperature in Fahrenheit? '))

# Convert the degrees in Fahrenheit to Celcius
# C = (f - 32) * 5/6
temp_in_celcius = (temp_in_fahrenheit - 32) * 5/9
print(f'The temperature in Celsius is {temp_in_celcius:.1f} degrees. \n')