"""
File: mealpricecalculator.py
Author: Emily Cordero

Purpose: Write a program to calculate the price of a meal.

Instructions: Compute the price of a meal as follows by asking for the price of child and adult meals, the number of each, and then the sales tax rate. Use these values to determine the total price of the meal. Then, ask for the payment amount and compute the amount of change to give back to the customer.

This is a continuation  of W03.

"""

# Welcome user to program 
print('Welcome to the Meal Price Calculator! \n')

# Ask the user for price of a child's and adults meal as floats
childs_meal_price = float(input("What is the price for a child's meal? "))
adults_meal_price = float(input("What is the price for an adult's meal? "))

# Ask user for drinks (creativity)
drinks = int(input('How many drinks of $2.50 each? '))

# Ask user how many appetizers they would like (creativity)
appetizers = int(input('How many appetizers of $1.25 each? '))

# Ask the user for the number of children and adults as ints
number_of_children = int(input('How many children are there? '))
number_of_adults = int(input('How many adults are there? '))

# Ask the user for the sales tax rate as a float
sales_tax_rate = float(input('What is the sales tax rate? '))

# Ask user if they would like to tip in percentage
tip_percentage = int(input('How much tip percentage would you like to give? '))

# Compute the meal subtotal before sales tax
# Multiply # of children by the price of meal and for adutls and add the two values together

total_price_children = number_of_children * childs_meal_price

total_price_adult = number_of_adults * adults_meal_price

total_price_appetizers = appetizers * 1.25

total_price_drinks = drinks * 2.50

subtotal = total_price_adult + total_price_children + total_price_appetizers + total_price_drinks

print()

# Display subtotal 
print(f'Subtotal: ${subtotal:.2f}')

# Compute the sales tax by multiplying the subtotal by the sales tax rate / 100
sales_tax = (subtotal * sales_tax_rate) / 100

# Display sales tax
print(f'Sales Tax: ${sales_tax:.2f}')

# Compute the total price by adding the subtotal and the sales tax
total_price = subtotal + sales_tax 

# calculate tip
tip_amount = total_price * (tip_percentage/100)

# Update total_price with tip
total_price = total_price + tip_amount

# Display tip
print(f'Tip: {tip_amount:.2f}')


# Display total of price
print(f'Total: ${total_price:.2f}')
print()

# Ask for the payment amount
payment_amount = float(input('What is the payment amount? '))

# Compute the remaining change to give
change = payment_amount - total_price
print(f'Change: ${change:.2f} \n')
