country_list = []
code_list = []
year_list = []
life_expectancy_list = []
total_life_exp = ''
average_life_exp = 0
max_country = ''
lowest_life_exp = 999999.00
life_exp = 1.0
max_life = -1.0
max_year = int
min_year = int
min_country = ''
min_life=99999999
max_code = int


user_year = int(input('Enter year of interest: '))
with open('life-expectancy.csv','r') as life_expectancy_file:
    first_line = life_expectancy_file.readline()
    next(life_expectancy_file)
    for line in life_expectancy_file:
        clean_line = line.strip()
        parts = clean_line.split(',')
        counter = 0
        
        country_list.append(parts[0])
        code_list.append(parts[1])
        year_list.append(parts[2]) 
        life_expectancy_list.append(float(parts[3]))

        for i in range(len(life_expectancy_list)):
            life_exp = life_expectancy_list[i]
            country = country_list[i]
            code = code_list[i]
            year = year_list[i]

        if life_exp > max_life:
            max_life = life_exp
            max_year = year
            max_country = country
            max_code = code 

        if life_exp <= min_life:
            min_life = life_exp
            min_country = country
            min_year = year
            min_code = code

    print(f'The overall max life expectancy is: {max_life:.5} from {max_country} in {max_year}')
    print(f'The overall max life expectancy is: {min_life:.5} from {min_country} in {min_year}')

    


    

        