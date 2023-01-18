"""
File: id.py
Author: Emily Cordero

Purpose: Write a program  write a program that will create a properly formatted ID badge.

"""

# Inform user to enter information
print('Please enter the following information: ')

# Adding a line
print()

# Ask user for first and last name, email address, phone number, job title, and id number

first_name = input('First name: ')
last_name = input('Last name: ')
email_address = input('Email address: ')
phone_number = input('Phone number: ')
job_title = input('Job title: ')
id_number = input('ID Number: ')
hair_color = input('Hair color: ')
eye_color = input('Eye Color: ')
date_hired = input('Month hired: ')
completed_training = input('Have you completed the orientation training? ')

# Adding a space
print()

# Print the ID card
print('The ID Card is: ')
print('------------------------------------')
print(last_name.upper() + ', ' + first_name.capitalize())
print(job_title.title())
print(f'ID: {id_number}')
print()
print(email_address.lower())
print(phone_number)

# Adding the stretch
print()
print(f'Hair: {hair_color:16} Eyes: {eye_color}')
print(f'Month: {date_hired:15} Training: {completed_training}')
print('------------------------------------')


