"""
File: mealpricecalculator.py
Author: Emily Cordero

Purpose: Write a program to calculate the price of a meal.

Instructions: Compute the price of a meal as follows by asking for the price of child and adult meals, the number of each, and then the sales tax rate. Use these values to determine the total price of the meal. Then, ask for the payment amount and compute the amount of change to give back to the customer.

"""

# Ask the user for price of a child's and adults meal as floats
childs_meal_price = float(input("What is the price for a child's meal? "))
adults_meal_price = float(input("What is the price for an adult's meal? "))

# Ask the user for the number of children and adults as ints
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("What is the number of adults? "))

# Ask the user for the sales tax rate as a float
sales_tax_rate = float(input("What is the sales tax rate? "))

# Compute the meal subtotal before sales tax
# Multiply # of children by the price of meal and for adutls and add the two values together

total_price_children = number_of_children * childs_meal_price
total_price_adult = number_of_adults * adults_meal_price
subtotal = total_price_adult + total_price_children

print()

# Display subtotal 
print('Subtotal: $' + str(subtotal))

# Compute the sales tax by multiplying the subtotal by the sales tax rate / 100
sales_tax = (subtotal * sales_tax_rate) / 100

# Display sales tax
print("Sales Tax: $" + str(sales_tax))

# Compute the total price by adding the subtotal and the sales tax
total_price = subtotal + sales_tax

# Display total of price
print("Total: $" + str(total_price))

# Ask for the payment amount
payment_amount = float(input('What is the payment amount? '))

# Compute the remaining change to give
change = payment_amount - total_price
print('$' + str(change))
