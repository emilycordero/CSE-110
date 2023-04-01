'''
Team Activity 
team.py 
Write functions to compute and return the areas of squares, rectangles and circles. 
'''
import math 

area = 0

def compute_area_square(side):
    area_of_square = compute_area_rectangle(side, side)
    return area_of_square

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return math.pi * (radius**2)

def compute_area(users_shape, val1, val2=0):
    area = -1

    if users_shape == 'square':
        area = compute_area_square(val1)
    elif users_shape == 'circle':
        area = compute_area_circle(val1)
    elif users_shape == 'rectangle':
        area = compute_area_rectangle(val1,val2)
    
    return area


# Loop to ask what the shape is
users_shape = ''

while users_shape != 'end':
    users_shape = input('What kind of shape do you have? ')

    if users_shape.lower() == 'square':
        side = float(input('What is the side of the square? '))
        shape = compute_area(users_shape,side)
        print(f'The area is {shape}. ')
    elif users_shape == 'rectangle':
        length = float(input('What is the length of the rectangle? '))
        width = float(input('What is the width of the rectangle? '))
        shape = compute_area(users_shape,length,width)
        print(f'The area is: {shape}')
    elif users_shape == 'circle':
        radius = float(input('What is the radius of the circle? '))
        shape = compute_area(users_shape,radius)
        print(f'The area is {shape}')
    
print('End of program')