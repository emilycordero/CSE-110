""" 
Author: Emily Cordero
File: shopping_cart.py 
Purpose: Create a program that stores a list of products in a shopping cart along with their prices. The user should have the ability to add items to the list, remove them, and see the total price of the cart.

"""
# Declare variables
menu = []
shopping_cart = []
add_item = ''
option = None

# Welcome user to the program
print('Welcome to the Shopping Cart Program!')

print()


while option != 5:
    # **Options for code**
    print('Please select one of the following: ')
    print('1. Add item\n 2. View cart\n 3. Remove item\n 4. Compute total\n 5. Quit')
    option = int(input('Please enter an action: '))

    # Add a new item
    while option == 1:
        add_item = str(input('What item would you like to add? '))
        shopping_cart.append(add_item)
        print(f"'{add_item}' had been added to the cart. ")
        print()
        print('Please select one of the following: ')
        print('1. Add item\n 2. View cart\n 3. Remove item\n 4. Compute total\n 5. Quit')
        option = int(input('Please enter an action: '))

    # Display the contents of the shopping cart
    while option == 2:
        print('The contents of the shopping cart are: ')
        for item in shopping_cart:
            print(item)
        print()
        print('Please select one of the following: ')
        print('1. Add item\n 2. View cart\n 3. Remove item\n 4. Compute total\n 5. Quit')
        option = int(input('Please enter an action: '))
    # Remove an item (only needed for the final project deliverable)

    # Compute the total (only needed for the final project deliverable)

# Quit
print('Thank you. Goodbye. ')