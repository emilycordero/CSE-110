""" 
file: wordgame.py
author: Emily Cordero

Purpose: Create a word game.

 """
# import random library
import random

 # Welcome user to the word guessing game

print('Welcome to the word guessing game! \n')

yes_game = input('Are you ready to begin (yes/no)? ')
# Declare variables
programming_words = ['javascript', 'python', 'java', 'c++', 'c#', 'php', 'html', 'css']
hint = ''
count = 0
correct_word = False

# Print the hint
while yes_game.lower() == 'yes':
    # Create the random word
    random_word = random.choices(programming_words)
    print(random_word)
    
    # Ask for the guess
    guessed_word = input('What is your guess? ')
    print(guessed_word)

    while guessed_word != random_word:
        count += 1
        correct_word = False
        guessed_word = input('What is your guess? ')
        print(guessed_word)

        if correct_word == True:
            print(f'Congratulations! You guessed it! It took you {count} times. \n ')
        else:
            correct_word == False

    yes_game = input('Are you ready to play again (yes/no)? ')

# Thank user
print('Thank you for playing. ')
