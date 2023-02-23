""" 
file: wordgame.py
author: Emily Cordero

Purpose: Create a word game.

 """
 # Welcome user to the word guessing game

print('Welcome to the word guessing game! \n')

play_again = input('Are you ready to begin (yes/no)? \n')

# Declare variables
secret = 'mosiah'
hint = ''
guess = ''
user_times_to_guess = 0

# While loop for game
while play_again.lower() == 'yes':
    print('Your hint is: ', end='')
    # Add hint
    for letter in secret:
        print('_', end='')

    print()
    print()

    # Ask for the guess
    guess = input('What is your guess? ')

    # while loop in case it is not correct word
    while guess != secret:
        guess = input('What is your guess? ')
        print(f'{hint}', end ='')
        for i, letter in enumerate(secret):
            # This is checking if we have a correct letter in the right place of the word
            if i < len(guess) and letter.lower() == (guess)[i]:
                hint += letter.upper()
            
            # Checks if the letter exists in the word but not the same place
            elif letter.lower() in guess:
                hint += letter.lower()
            
            # This letter is incorrect in the secret word
            else:
                hint += '_'
        print(f'{hint}', end ='')    
    
    # Space
    print()
    print()

    play_again = input('Do you want to play again (yes/no)? \n')
# Thank user
print('Thank you for playing. ')
