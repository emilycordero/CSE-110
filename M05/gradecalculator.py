"""
File: ifstatements.py
Author: Emily Cordero

Purpose: Write a program that will work as a grade calculator. 

"""

# Ask user for percentage
grade_percent = float(input('What is your grade percentage? '))

# If statement to compare grades

if grade_percent >= 90:
    letter = 'A'
elif grade_percent >= 80:
    
    letter = 'B'
elif grade_percent >= 70:
    letter = 'C'
elif grade_percent >= 60:
    letter = 'D'
else:
    letter = 'F'

grade_variable = grade_percent % 10

if grade_variable >= 7:
    grade_variable = '+'
elif grade_variable < 3:
    grade_variable = "-"
else:
    grade_variable= ''

# Stetch 2 take off sign for >93
if grade_percent >= 93:
    grade_variable = ''

# Stretch 3 - take off sign for F-

if letter == 'F':
    grade_variable = ''

print(f'Your letter grade is: {letter}{grade_variable}')
# If statement to determine passing

if grade_percent >= 70:
    print('You are passing! Great job.')
else:
    print('You are failing. Better luck next time!')



