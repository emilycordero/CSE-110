# Purpose: ask user for a series of numbers and append eachone to a list stop when they enter 0

# Print a statement 
print('Enter a list of numbers, type 0 when finished. ')

new_number = []
user_number = None
number_total = 0

while user_number != 0:
    # Ask user for a number 
    user_number = int(input('Enter number: '))
    
    # If it = to 0 append
    if user_number != 0:
        new_number.append(user_number)

# Calculate the sum
for number in new_number:
    number_total += number
print(f'The sum is: {number_total}')

# Caclculate average of the numbers in the list
average_number = number_total / len(new_number)
print(f'The average is: {average_number}')

# Use max to calculate the largest number
max_number = max(new_number)
print(f'The largest number is: {max_number}')

# Smallest number
smallest_number = 9999999999

# Find smallest positive number: Stretch 1
for number in new_number:
    if number > 0 and number < smallest_number:
        smallest_number = number
print(f'The smallest positive number is: {smallest_number}')

# Sorted numbers
sorted_numbers = sorted(new_number)
print(f'The sorted list is: {sorted_numbers}')


    

