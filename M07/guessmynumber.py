import random

# Create a variable for the play_again
play_again = 'yes'

# Create a while loop 
while play_again.lower() == 'yes':
    magic_number = random.randint(1, 100)
    guess = -1
    count = 0
    while guess != magic_number:
        guess = int(input('What is your guess? '))
        count += 1
        if guess > magic_number:
            print('Lower')
        elif guess < magic_number:
            print('Higher')
        else:
            print('You guessed it!')
            print(f'You guessed {count} times.')
    play_again = input('Do you want to play again (yes/no)? ')

print('Thanks for playing! ')
