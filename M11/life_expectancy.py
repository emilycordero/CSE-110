country_list = []
code_list = []
year_list = []
life_expectancy_list = []



with open('life-expectancy.csv') as life_expectancy_file:
    for line in life_expectancy_file:
        clean_line = line.strip()
        parts = clean_line.split(',')

        country = parts[0]
        code = parts[1]
        year = parts[2] 
        life_expectancy = parts[3]

        max_life = max(life_expectancy)
        print(f'The overall max life expectancy is: {max_life}')
        min_life = min(life_expectancy)
        print(f'The overall min life expectancy is: {min_life}')

        