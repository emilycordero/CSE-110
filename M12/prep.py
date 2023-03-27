numbers = [42,25,18,83,23,85,38,2]

largest_so_far = numbers[0]

for number in numbers:
    if number > largest_so_far:
        largest_so_far = number
print(f'The largest is: {largest_so_far}')

shopping_cart = [
    ['Chips',2.99],
    ['Bread', 2.50],
    ['Milk', 3.19],
    ['Ice Cream', 6.99],
    ['Cheese', 5.99],
    ['Candy Bar', 0.99]
]

max_price = -1
max_product = ''

for item in shopping_cart:
    product_name = item[0]
    price = item[1]

    if price > max_price:
        max_price = price
        max_product = product_name
print(f'The max product and price is: {max_product}: {max_price}')
