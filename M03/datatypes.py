# To get current date/time use datetime library
from datetime import datetime, timedelta

first_num = 6
second_num = 2

print(first_num + second_num)
print(first_num - second_num)
print(first_num * second_num)
print(first_num / second_num)
print(first_num ** second_num)

days_in_feb = 28
print(str(days_in_feb) + ' days in February.')

first_num_user = input('Enter 1st number: ')
second_num_user = input('Enter 2st number: ')
print(int(first_num_user) + int(second_num_user))
print(float(first_num_user) + float(second_num_user))

color = 'blue'
animal = 'horse'

print(color + animal)
# Displays bluehorse

combined_words = color + ' ' + animal + '!'
print(combined_words)

# Displays date
current_date = datetime.now()
print('Current date: ' + str(current_date))
print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))


today = datetime.now()
print('Today is: '+ str(today))

#timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

# When a user gives a date
birthday = input('When is your birthday (dd/mm/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print ('Birthday: ' + str(birthday_date))

