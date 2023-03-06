'''
Emily Cordero
check.py 
Practice working with list indexes.

'''
items = []
item = ''
indexes = []

print('Please enter the items of the shopping list (type: quit to finish):')

while item.lower() != 'quit':
    item = input('Item: ')
    if item.lower() != 'quit':
        items.append(item)

print('The shopping list: ')

for i in range(len(items)):
    item = items[i]
    print(f'{item}')

print('The shopping list with indexes is: ')
for i in range(len(items)):
    item = items[i]
    print(f'{i}. {item}')

print()
replace = int(input('What item would you like to change? '))
new_item = input('What new item would you like? ')

items[replace] = new_item

print('The shopping list: ')

for i in range(len(items)):
    item = items[i]
    print(f'{i}: {item}')

