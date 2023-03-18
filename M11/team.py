'''
EMily COrdero
team.py 
Practice with group on files.
'''
with open('hr_system.txt') as hr_file:
    for line in hr_file:
        # remoce /n
        clean_line = line.strip()
        parts = clean_line.split()

        name = parts[0]
        id = parts[1]
        title = parts[2]
        salary = float(parts[3])

        pay_amount = salary / 24

        #Engineering bonus
        if title.lower() == 'engineer':
            pay_amount += 1000
        print(f'{name} (ID: {id}), {title} - ${pay_amount:.2f}')