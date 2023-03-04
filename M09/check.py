""" 
file: team.py
author: Emily Cordero

Purpose: Ask the user for the names of their friends and append them to a list. Then, display each of the friends in the list. You should stop asking for friends when the user types "end".

 """
user_friends = []
user_typed = ''

while user_typed != 'end':
    user_typed = str(input('Type the name of a friend: '))
    if user_typed != 'end':
        user_friends.append(user_typed)
print('Your friends are: ')

for friend in user_friends:
    print(friend)