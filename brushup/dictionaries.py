# dictionaries

person = {'name':'John', 'age':18}

print(person['name'])
print(person['age'])


# methods
print(person.get('name'))

print(person.keys())
print(person.values())

print('age' in person.values())
person.update({'name': 'Rui', 'age':22})
print(person)

# clearing a dictionary

person.clear()
print(f'cleared: {person}')