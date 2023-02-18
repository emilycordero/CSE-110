""" 
file: wordgame.py
author: Emily Cordero

Purpose: Create a word game.

 """
 # Welcome user to the word guessing game

print('Welcome to the word guessing game! \n')

play_again = input('Are you ready to begin (yes/no)? \n')

# Declare variables
secret = 'python'

# While loop for game
while play_again.lower() == 'yes':
    count = 0
    
    # Ask for the guess
    guessed_word = input('What is your guess? ')

    while guessed_word.lower() != secret:
        count += 1
        print('This guess was not correct. ')
        guessed_word = input('What is your guess? ')

    print(f'Congratulations! You guessed it! It took you {count} times. \n ')

    play_again = input('Are you ready to play again (yes/no)? ')

# Thank user
print('Thank you for playing. ')
