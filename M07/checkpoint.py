""" 
File: checkpoint.py
Author: Emily Cordero

Purpose: Demonstrate your understanding of loops by completing the following individual checkpoint assignment.

 """

 # Ask user for a positive number using a while loop
number = 0

number = int(input('Please type a positive number: '))

while number <= 0:
    print('Sorry, that was a negative number. Try again. ')
    number = int(input('Please type a positive number: '))

# Print a statement for when the loop ends
print(f'The number is: {number}')

#  Create a while loop to simulate a child asking parent for candy
yes_candy = 'no'

while yes_candy.lower() == 'no':
    yes_candy = input('May I have a piece of candy? ')

# Print thank you at end of loop
print('Thank you. ')

""" 
yes_candy = ''

while yes_candy != 'yes':
    yes_candy = input('May I have a piece of candy? ')

print('Thank you.')
 """