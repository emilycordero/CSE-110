print()

# Secret word
secretword = 'house'

# Counts attempts made
count = 0

# guess by user
guess=''

# Play again loop
play_again = ''
# Welcoming message for user
print('Welcome to my word game')

play_again = input('Do you want to play? ')

while play_again.lower() == 'yes':
    # hint
    print('Your hint is: ',end='')
    for letter in secretword:
        print('_',end='')

    # SPace
    print()

    # While loop for when guess does not match secretWord
    while guess != secretword:
        count += 1
        guess = input('What is your guess? ')
        hint= ''

        while len(guess) != len(secretword):
            count += 1
            print('Sorry, the guess must be the same length as secret word.')
            guess = input('What is your guess? ')

        for i, letter in enumerate(guess):
            if i < len(guess) and letter.lower() == (secretword)[i]:
                hint += letter.upper()
            elif letter.lower() in secretword:
                hint += letter.lower()
            else:
                hint += '_'
        print(f'Your hint is {hint}')

    print('Congratulations! You guessed it.')
    print(f'You guessed {count} times.')
    play_again = input('Do you want to play again? ')