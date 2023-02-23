""" 
file: wordgame.py
author: Emily Cordero

Purpose: Create a word game.

"""
# Have a secret word stored in the program
secret_word = 'mosiah'

# Declare attempts made
attempts_made = 0

# Error statement
wrong_guess = 'Your guess was not correct.'

# Prompt the user for a guess
guess = str(input('What is your guess? '))

# continue looping as long as that guess is NOT correct
while guess != secret_word:
    # Calculate the number of guess and display it in the end
    attempts_made += 1
    print(wrong_guess)
    guess = str(input('What is your guess? '))
    hint = ''


print('Congratulations! You guessed it!')
print(f'It took you {attempts_made} guesses.')
