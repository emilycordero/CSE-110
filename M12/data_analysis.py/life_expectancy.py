country_list = []
code_list = []
year_list = []
life_expectancy_list = []
total_life_exp = ''

user_year = int(input('Enter year of interest: '))
with open('life-expectancy.csv') as life_expectancy_file:
    for line in life_expectancy_file:
        clean_line = line.strip()
        parts = clean_line.split(',')
        counter = 0

        country_list.append(parts[0])
        code_list.append(parts[1])
        year_list.append(parts[2]) 
        life_expectancy_list.append(parts[3])
        max_life = max(life_expectancy_list)
        min_life = min(life_expectancy_list)
    print(f'The overall min life expectancy is: {min_life}')
    print(f'The overall max life expectancy is: {max_life}')

        