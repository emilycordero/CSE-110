""" list = []
item = ''
quit = 'quit'

quit = input('Do you want to start? ')
while item != 'quit':
    item = input('Enter an item: ')
    list.append(item)

for item in list:
    print(item) """

x = 5
x =+ 1
print(x)

my_list = [1, 2, 3, 4, 5, 6]

largest = 0

for value in my_list:

    if value > largest:

        largest = value

print(f"The largest is {largest}")

smallest = 9999999999999

for value in my_list:

    if value <= smallest:

        smallest = value

print(f"The smallest is {smallest}")