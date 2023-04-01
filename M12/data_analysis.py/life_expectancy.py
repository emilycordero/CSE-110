country_list = []
code_list = []
year_list = []
life_expectancy_list = []
counter = 0
total_life_exp = 0
average_life_exp = 0
life_exp = 1.0
user_max_country = ''
user_max_life = -1.0
user_max_year = int
user_max_code = int
user_min_year = int
user_min_country = ''
user_min_life= 99999999
max_country = ''
max_life = -1.0
max_year = int
max_code = int
min_year = int
min_country = ''
min_life= 99999999



user_year = int(input('Enter year of interest: '))
with open('life-expectancy.csv','r') as life_expectancy_file:
    first_line = life_expectancy_file.readline()
    next(life_expectancy_file)
    for line in life_expectancy_file:
        clean_line = line.strip()
        parts = clean_line.split(',')
        counter += 1
        country_list.append(parts[0])
        code_list.append(parts[1])
        year_list.append(parts[2]) 
        life_expectancy_list.append(float(parts[3]))

        for i, life_exp in enumerate(life_expectancy_list):
            life_exp = life_expectancy_list[i]
            country = country_list[i]
            code = code_list[i]
            year = year_list[i]

        if life_exp > max_life:
            total_life_exp += life_exp
            max_life = life_exp
            max_year = year
            max_country = country
            max_code = code

        if life_exp <= min_life:
            min_life = life_exp
            min_country = country
            min_year = year
            min_code = code
        average_life_exp = total_life_exp / counter
        while year == user_year:
            if life_exp > max_life:
                user_max_life = life_exp
                user_max_year = year
                user_max_country = country
                user_max_code = code

            if life_exp <= min_life:
                user_min_life = life_exp
                user_min_country = country
                user_min_year = year
                user_min_code = code

    print(f'The overall max life expectancy is: {max_life:.5} from {max_country} in {max_year}')
    print(f'The overall max life expectancy is: {min_life:.5} from {min_country} in {min_year}')

    print()

    print(f'For the year of {user_year}: ')
    print(f'The average life expectancy across all countries was {average_life_exp}')
    print(f'The max life expectancy was in {user_max_country} with {user_max_life}')
    print(f'The min life expectancy was in {user_min_country} with {user_min_life}') 