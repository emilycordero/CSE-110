'''
Emily Cordero
team.py 
Practice opening files and iterating through lines. 
'''

largest_chapter = -1
largest_scripture = ''
largest_book = ''

chosen_volume = input('What volume of the scripture do you want to learn more about? ')

with open('books_and_chapters.txt') as book_file:
    for line in book_file:
        clean_line = line.strip()
        parts = clean_line.split(':')

        scripture = parts[2]
        chapter = int(parts[1])
        book = parts[0]
        if scripture.lower() == chosen_volume.lower():
            print(f'Scripture: {scripture}, Book: {book}, Chapters: {chapter}')
            if chapter > largest_chapter:
                largest_chapter = chapter
                largest_scripture = scripture
                largest_book = book
    print(f'The largest book in {chosen_volume} is: {largest_book} with {largest_chapter} chapters.')
        #print(f'Scripture: {scripture}, Book: {book}, Chapters: {chapter}')

