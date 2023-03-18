# with statement takes out following statement : courses_file = open("course.txt")

with open("course.txt") as courses_file:
    for line in courses_file:
        # Line = "Course, Grade"
        parts = line.split(',')
        
        # Parts = ['Course', 'Grade']
        name = parts[0]
        grade = float(parts[1])

        bonus_grade = grade +3

        print(f'{name} - Grade: {grade}, after bonus: {bonus_grade}')
print('Goodbye')

