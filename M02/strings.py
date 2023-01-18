# strings can be stored in variables
""" first_name = 'Emily'
last_name = 'Cordero'
sentence = 'The dog ate the homework'
print(first_name + last_name)
print('Hello ' + first_name + last_name)
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a')) """

# Format strings 
user_first_name = input('What is your first name? ')
user_last_name = input('What is your last name? ')
print('Hello ' + user_first_name.capitalize() + ' ' + user_last_name.capitalize())

# Adding place holders 
output = f'Hello, {user_first_name} {user_last_name}'
output2 = 'Hello, {} {}'.format(user_first_name,user_last_name)
output3 = 'Hello, {0} {1}'.format(user_first_name, user_last_name)
print(output)
print(output2)
print(output3)