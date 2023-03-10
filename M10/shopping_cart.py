""" 
Author: Emily Cordero
File: shopping_cart.py 
Purpose: Create a program that stores a list of products in a shopping cart along with their prices. The user should have the ability to add items to the list, remove them, and see the total price of the cart.

"""
# Declare variables
quantity_of_items = []
prices_of_items = []
shopping_items = []
shopping_cart = []
add_item = ''
option = None
sales_tax_rate = 8.2


# Welcome user to the program
print()

print('Welcome to the Shopping Cart Program!')

print()

print('Please select one of the following: ')
print('1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit')
option = int(input('Please enter an action: '))

while option != 5:
    # **Options for code**
    # Add a new item
    while option == 1:
        add_item = str(input('What item would you like to add? '))
        shopping_items.append(add_item)
        price_of_item = float(input(f"What is the price of '{add_item}'? "))
        prices_of_items.append(price_of_item)
        quantity_of_item = int(input('How many would you like of the item? '))
        quantity_of_items.append(quantity_of_item)
        print(f"{quantity_of_item} of '{add_item}' has been added to the cart. ")
        print()
        print('Please select one of the following: ')
        print('1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit')
        option = int(input('Please enter an action: ')) 

    # Display the contents of the shopping cart
    while option == 2:
        print('The contents of the shopping cart are: ')
        for i in range(len(shopping_items)):
            item = shopping_items[i]
            price = prices_of_items[i]
            number = quantity_of_items[i]
            i += 1
            print(f'{i}. {number} of {item} - ${price:.2f} each.')
        print()
        print('Please select one of the following: ')
        print('1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit')
        option = int(input('Please enter an action: '))
    # Remove an item 
    while option == 3:
        for i in range(len(shopping_items)):
            item = shopping_items[i]
            price = prices_of_items[i]
            number = quantity_of_items[i]
        remove = int(input('What item would you like to remove? '))
        while remove > len(shopping_items):
            print('Sorry, that is not a valid item number. ')
            remove = int(input('What item would you like to remove? '))
        
        amount_removed = int(input('How many would you like to remove? '))
        if remove <= len(shopping_items) and amount_removed == number:
            shopping_items.pop((remove -1))
            prices_of_items.pop((remove -1))
            quantity_of_items.pop((remove-1))
            print('Item removed.')
        elif remove <= len(shopping_items) and amount_removed < number:
            print(f'{amount_removed} of {item} was removed.')
            number -= amount_removed
            quantity_of_items.insert(0,number)
        else:
            print('Sorry, that is not a valid amount. ')
        print()
        print('Please select one of the following: ')
        print('1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit')
        option = int(input('Please enter an action: '))
    # Compute the total 
    # Added sales tax of wa state in my town 8.2%
    while option == 4:
        subtotal = 0
        for i in range(len(shopping_items)):
            item = shopping_items[i]
            price = prices_of_items[i]
            number = quantity_of_items[i]
            subtotal += price * number
        sales_tax = subtotal * (sales_tax_rate/100)
        total_price = subtotal + sales_tax
        print(f'The subtotal is: ${subtotal:.2f}')
        print(f'The sales tax is: ${sales_tax:.2f}')
        print(f'The total price of the items in the shopping cart is ${total_price:.2f}')
        print()
        print('Please select one of the following: ')
        print('1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit')
        option = int(input('Please enter an action: '))
# Quit
print('Thank you. Goodbye. ')
