people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
youngest_person_age = 999999999
youngest_person_name = ''


for line in people:
    parts = line.split(' ')
    name = parts[0]
    age = int(parts[1])

    if age <= youngest_person_age:
        youngest_person_age = age
        youngest_person_name = name
print(f' Youngest person is: {youngest_person_name}, {youngest_person_age}')

