'''
Emily Cordero
prep.py
Pupose: Learn how to access items in a list at any location, and also how to remove items.
'''

the_list = [0,1,2,3,4,5]
first = the_list[0] # Gets 1st item
second = the_list[1] # gets second item

index = int(input('Which index would you get? '))
user_choice = the_list[index] # gets the item at the index the user typed

# ITERATING THROUGH A LIST USING AN INDEX
number_of_items = len(the_list)

for i in range(len(the_list)):
    item = the_list[i]
    print(item)

# Parallel lists: following example was created using the assignment due this week 
names = []
numbers = []
user_name = ''
option = 0

# Code to generate the lists
while option != 5:
    # **Options for code**
    print('Please select one of the following: ')
    print('1. Add item\n 2. View cart\n 3. Remove item\n 4. Compute total\n 5. Quit')
    option = int(input('Please enter an action: '))
    while option == 1:
        # Ask user for a number 
        user_name = str(input('Enter name: '))
        user_number = float(input('Enter price: '))
        print()
        print('Please select one of the following: ')
        print('1. Add item\n 2. View cart\n 3. Remove item\n 4. Compute total\n 5. Quit')
        option = int(input('Please enter an action: '))
        
        # If it = to 0 append
        if user_name != 'end':
            names.append(user_name)
            numbers.append(user_number)
    while option == 2:
        for i in range(len(names)):
            name = names[i]
            number = numbers[i]

            print(f'{name}: {number}')
        print()
        print('Please select one of the following: ')
        print('1. Add item\n 2. View cart\n 3. Remove item\n 4. Compute total\n 5. Quit')
        option = int(input('Please enter an action: '))

print('Thank you, goodbye.')

# Removing items from a list

the_list.pop(3) # Removes item at index 3
for item in the_list:
    print(item, end = '')
print()
the_list.pop() # Removes the last item
for item in the_list:
    print(item, end='')

