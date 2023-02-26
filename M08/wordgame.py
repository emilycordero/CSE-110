""" 
file: wordgame.py
author: Emily Cordero

Purpose: Create a word game.

"""
# Import random library to be able to use random.choice() function
import random

# Run again loop
run_again = 'yes'

# Have a secret list stored in the program
secret_list = ['python', 'c++', 'c#', 'html', 'css', 'java', 'javascript', 'mosiah', 'moroni', 'temple']

# Declare attempts made
attempts_made = 0

# Error statement
wrong_guess = 'Your guess was not correct.'

# Guess
guess = ''

# Start loop
run_again = input('Do you want to play Wordle (yes/no)?')

# Run again loop
while run_again.lower() == 'yes':
    # To randomly select a word
    secret_word = random.choice(secret_list)

    # Loop for initial hint
    print('Your hint is: ', end='')
    for letter in secret_word:
        print('_ ', end='')

    # Space     
    print()
    print()

    # continue looping as long as that guess is NOT correct

    while guess.lower() != secret_word:
        # Calculate the number of guess and display it in the end
        attempts_made += 1
        guess = str(input('What is your guess? '))
        hint = ''

        while len(guess) != len(secret_word):
            attempts_made += 1
            print('Sorry, the guess must have the same number of letters as the secret word.')
            guess = str(input('What is your guess? '))

        for i, letter in enumerate(guess):
            if i < len(guess) and letter.lower() == (secret_word)[i]:
                hint += letter.upper()
            elif letter.lower() in secret_word:
                hint += letter.lower()
            else:
                hint += '_ '
        print(f'Your hint is: {hint}')

    print()
    print('Congratulations! You guessed it!')
    print(f'It took you {attempts_made} guesses.')
    
    print()
    run_again = input('Do you want to play again (yes/no)?')
print()
print('Thank you for playing my game!')