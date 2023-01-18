"""
File: madlibs.py
Author: Emily Cordero

Purpose: Write a program  that will implement a program that asks the user for a series of words and then displays the story with the user's words inserted into the appropriate places

"""
# Tell the user to enter info
print('Please enter the following: ')
print()
adjective = input('adjective: ')
animal = input('animal: ')
verb1 = input('verb: ')
exclamation = input('exclamation: ')
verb2 = input('verb: ')
verb3 = input('verb: ')
object = input('object: ')
body_part = input('human body part: ')
exclamation_2 = input('Another exclamation: ')
adjective_2 = input('Another adjective: ')


print()

print('Your story is: ')

print()

# Print story and the outputs
print(f'The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb1} down the hallway. "{exclamation.capitalize()}!" I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3} right in front of my family. Then all of a sudden, a {object} knocked me right on the {body_part}. "{exclamation_2.capitalize()}!" I screamed in pain. What a {adjective_2} day.')