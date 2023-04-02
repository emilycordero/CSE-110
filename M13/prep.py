from datetime import datetime

def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = 'Susan'
print_time('completed function')

for x in range(0,10):
    print(x)
print_time('completed for loop')

first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name)

middle_name = input('Enter your middle name: ')
middle_name_initial = get_initial(middle_name)

last_name = input('Enter your last name: ')
last_name_initial = get_initial(last_name)

print('Your initials are: ' + first_name_initial + middle_name_initial + last_name_initial)