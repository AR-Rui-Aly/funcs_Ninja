# joining lists
fruits = ['banana', 'apple', 'pear', 'peach']
car_brands = ['bmw', 'mercedes', 'samurai']


new_combinations = fruits + car_brands
print(new_combinations)

# the extends method alters the object
fruits.extend(car_brands)
print('extended fruits:', fruits)

print(fruits)
print(car_brands)

#slicing lists

