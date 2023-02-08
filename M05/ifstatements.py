"""
File: ifstatements.py
Author: Emily Cordero

Purpose: Write a program to practice if statements ( conditional logic).
"""
""" price = float(input('What is the price? '))

if price >= 1.00:
    tax = 0.07
    print('Tax rate is: ' + str(tax))
else: 
    tax = 0
    print('Tax rate is: ' + str(tax)) """

# Be careful when comparing strings, must convert to compare
country = input('What country are you from? ')

if country.lower() == 'Canada':
    if country == 'canada':
        print('Oh you are a Canadian!')
    else:
        print('You are not from Canada')

# Complicated conditionals
if country.lower() == 'usa':
    state = input('What state are you from? ')
    
    if state in('Washington', 'Virginia', 'California'):
        tax = 0.068
    elif state == 'Oregon':
        tax = 0
    else:
        tax = 0.15

else:
    tax = 0
    
print('Your tax rate is: ' + str(tax))



