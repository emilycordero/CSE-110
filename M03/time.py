# To get current date/time use datetime library
from datetime import datetime, timedelta

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