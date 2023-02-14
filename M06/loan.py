""" 

File: loan.py
Author: Emily Cordero

Purpose: Create a program that will determine a user if they can qualify for a loan. 

 """
 # Boolean for loan
qualify_loan = False

 # Ask user for a rating from 1-10 on the following question
loan = int(input('How large is the loan? '))

credit_history = int(input('How good is your credit history? '))

income = int(input('How high is your income? '))

down_payment = int(input('How large is the down payment? '))

# If statement using boolean
if loan > 5:
    if credit_history >= 7 and income >= 7:
        qualify_loan = True
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            qualify_loan = True
        else:
            qualify_loan = False
    else:
        qualify_loan = False

elif loan <= 5:
    if credit_history < 5: 
        if income or down_payment >= 7:
            qualify_loan = True
        elif income and down_payment >= 4:
            qualify_loan = True
        else:
            qualify_loan = False
    else:
        qualify_loan = False
else:
    qualify_loan = False

# Print the decision
if qualify_loan == True:
    print('You qualify for a loan!')
else:
    print('You do not qualify for a loan...')