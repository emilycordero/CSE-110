'''
Emily Cordero
team.py
Purpose: you will track bank accounts and the balances in each one.
'''
names = []
balances = []
highest_name = ''
highest_balance = 0
name = ''
total = 0
average = 0
print()

print('Enter the names and balances of bank accounts (type: quit when done)')

while name != 'quit':
    name = input('What is the name of this account? ' )
    if name != 'quit':
        names.append(name)
        balance = float(input('What is the balance '))
        balances.append(balance)
print()
print('Account Information: \n')
for i in range(len(names)):
    name = names[i]
    balance = balances[i]
    total += balances[i]
    average = total / len(names)
    print(f'{i}. {name} - {balance}')
    if balances[i] > highest_balance:
        highest_balance = balances[i]
        highest_name = names[i]
print(f'Total: ${total:.2f}')
print(f'Average: ${average:.2f}')
print(f'Highest balance: {highest_name} - {highest_balance}')

print()

update = 'yes'
while update == 'yes':
    update = input('Do you want to update an account? ')
    if update == 'yes':
        i_name = int(input('Which account do you want to update? '))
        new_balance = float(input('What is the new balance? '))

        balances[i] = new_balance
    print('Account Information: ')
    for i in range(len(names)):
        name = names[i]
        balance = balances[i]
        print(f'{i}. {name} - {balance:.2f}')
