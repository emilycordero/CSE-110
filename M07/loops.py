tip = float(input('What is the tip amount? '))

# We are practicing while loops
while tip < 0:
    print('Sorry, the tip cannot be negative. ')
    tip = float(input('What is the tip amount? '))

print(f'You have tipped an amount of ${tip}. ')

number = 0

# Keep looping as long as the nummber is less than 10
while number < 10:
    number = int(input('What is the number? '))

print('Finished with the loop. ')

# Have the program count
number = 1
name = ''

while number <= 5:
    print(f'The number is: {number}')
    name = input('What is your name? ')
    number = number + 1

print('Finished with the loop. ')



