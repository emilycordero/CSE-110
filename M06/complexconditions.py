""" 
File: complexconditions.py
Author: Emily Cordero

Purpose: To practice if statements. 

"""

x = int(input('What is x? '))
y = int(input('What is y? '))
word = input('Enter a word: ')
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
is_hot = True

# Conditions: and / or
if x > 5 and x < 10:
    # This happens if both conditions are true
    print('This statement is true! ')
if x > 5 or y > 10:
    # This happens if either or both are true
    print('This statement is true! ')

if (x > 5 or x < -5) and y > 10:
    # X can either be greater 5 or less than -5 and y must be greater than 10
    print('This statement is true! ')

if x > 5 and y > 10 and word.lower() == 'taco':
    # This happens if all are true
    print('This statement is true! ')

# Testing similar conditions

# Do not put if x == 5 or 6
if x == 5 or x == 6:
    print('This is true.')

# To compare multiple conditions
if first_name == 'Scott' or last_name == 'Joe':
    print('Scott Joe')
else:
    print('Your name is not Scott Joe.')

if is_hot:
    print("It's hot.")
elif not is_hot:
    print("It is not hot.")
else:
    print("Not is hot")