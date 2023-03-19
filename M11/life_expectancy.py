country_list = []
code_list = []
year_list = []
life_expectancy_list = []

run_again = input('Do you want to know life expectancies of countries around the world? ')

while run_again == 'yes':
    with open('life-expectancy.csv') as life_expectancy_file:
        for line in life_expectancy_file:
            clean_line = line.strip()
            parts = clean_line.split(',')

            # Create variables for the parts
            countries = parts[0]
            for country in countries:
                country_list.append(country)
            codes = parts[1]
            for code in codes:
                code_list.append(code)
            years = parts[2]
            for year in years:
                year_list.append(year)
            life_expectancy = parts[3]
            for life_exp in life_expectancy:
                life_expectancy_list.append(life_exp)
        for i in range(len(country_list)):
            country = country_list[i]
        for code_i in range(len(code_list)):
            code = code_list[code_i]
        for year_i in range(len(year_list)):
            year = year_list[year_i]
        for life_i in range(len(life_expectancy_list)):
            life_exp = life_expectancy_list[life_i]
                
        year_of_interest = int(input('Enter the year of interest: '))
        while year_of_interest != year_list:
            max_life = max(life_expectancy)
            print(f'The overall max life expectancy is: {max_life}')
            min_life = min(life_expectancy)
            print(f'The overall min life expectancy is: {min_life}')
    run_again = input('Do you want to look at another year of interest? ')
        
