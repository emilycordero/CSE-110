"""
File: parkride.py
Author: Emily Cordero   

Purpose: As a team to write a program for a fictitious amusement park ride.

"""

# Boolean 
can_ride = False

# Ask for rider 1's age and height
rider1_age = int(input('What is the age of the first rider? '))
rider1_height = int(input('What is the height of the first rider? '))

# Stretch 2 -- If statement for the golden passport 
if rider1_age >= 12 and rider1_age <= 17:
    golden_passport1 = input('Do you have a golden passport (yes/no)? ')
# Ask if there is a second rider
if_rider2 = input('Is there a second rider (yes/no)? ')

# if there is a second rider ask for height and age
if if_rider2.lower() == 'yes':
    rider2_age = int(input('What is the second riders age?' ))
    rider2_height = int(input('What is the height of the second rider? '))
    if rider1_age >= 12 and rider1_age <= 17:
        golden_passport2 = input('Does the second rider have a golden passport (yes/no)? ')  
    elif rider1_height < 36 or rider2_height < 36:
        can_ride = True
    else:    
        if rider1_age >= 12 and rider1_height >= 52 and rider2_age >= 12 and rider2_height >= 52:
            can_ride = True
        else:
            can_ride = False
else: 
    if rider1_age >= 18 and rider1_height >= 62:
        can_ride = True
    else:
        can_ride = False
if (rider1_age > 11 and rider1_age < 18)  or (rider2_age > 11 and rider2_age < 18) and (golden_passport1.lower() == 'yes' or golden_passport2.lower() == 'yes'):
            can_ride = True

else:
    can_ride = False

# Print out whether rider can or cannot ride. 
if can_ride:
    print('You can ride! ')
else:
    print('You can not ride.')

