# Looping with condition
names = ['cordero', 'Emily']
index = 0
while index < len(names):
    print(names[index])

    # Change the condition!! or else infinite
    index = index + 1

# Notes from pages
items = ["crayon", "scissors", "paper", "glitter glue", "markers", "pens"]

for item in items:
    print(f'The item is: {item}')

# Instead of this numbers = [0,1,2,3,4,5,6,7,8,9] use this:
numbers = range(10)

for number in range(10):
    print(number)

# Will start with 100 and go up to 199 
for i in range(100, 200):
    print(i)

# Will do the same but count by 10's
for i in range(100,200,10):
    print(i)

# We can also use inner loops to have -- characters in front of it

for i in range(5):
    print(i)
    for j in range(10, 13):
        print(f"--{j}")
        # We generally use i for the first loop, then j and if there was a third it would be k.

# You can iterate through names
first_name = "Emily"

""" for letter in first_name:
    print(f'The letter is: {letter}') """
# Use Python Enumerate
for i, letter in enumerate(first_name):
    print(f'The {letter} is at position {i}')

# Accessing letters by position: 3 index will get 4th letter not 3rd
fourth_letter = first_name[3] # Notice, using 3 instead of 4
print(fourth_letter)

# Iterating through each letter using index
word = "book"
number_of_letters = 4

for index in range(number_of_letters):
    letter = word[index]
    print(f'Index: {index} Letter: {letter}')

# Finding the string length
dog_name = input("What is your dog's name? ")
letter_count = len(dog_name)
print(f"Your dog's name has {letter_count} letters. ")
