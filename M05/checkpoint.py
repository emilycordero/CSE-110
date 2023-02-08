"""
File: ifstatements.py
Author: Emily Cordero

Purpose: Write a program to practice if statements ( conditional logic).

uSED https://www.w3schools.com/python/python_operators.asp as a reference.
"""

# Ask user for first number
first_number = float(input('What is the first number? '))

# Ask user for second number
second_number = float(input('What is the second number? '))

# Use if statement to compare number
if first_number > second_number:
    print('The first number is greater. ')
else:
    print('The first number is not greater. ')

if first_number == second_number:
    print('The numbers are equal. ')
else:
    print('The numbers are not equal. ')

if first_number < second_number:
    print('The second number is greater. ')
else:
    print('The second number is not greater. ')

# Hard code fav animal 
fav_animal = 'bear'

user_fav_animal = input('What is your favorite animal? ')
if user_fav_animal.lower() == fav_animal:
    print('That is my favorite animal too! ')
else:
    print('That is a cool animal. ')