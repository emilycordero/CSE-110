""" 
file: team.py
author: Emily Cordero

Purpose: Write a program that asks the user for their favorite letter. Then, loop through a programmed word one letter at a time. If the letter in the programmed word is the user's favorite, print it out as a capital letter (or "hide" it), if not, print it out as a lower case letter.

 """
word = 'commitment'
fav_letter = input('What is your favorite letter? ')

# BIG differencce in code when i switch == m to != m
for letter in word:
    if letter != fav_letter.lower():
        print(f'{letter.lower()}', end='')
    else:
        print('_', end='')
