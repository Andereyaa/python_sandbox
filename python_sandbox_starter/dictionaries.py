# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# create dictt
person = {
    'first_name' : 'John',
    'last_name' : 'Doe',
    'age' : 30,
}
print(person, type(person))

# use constructor
person2 = dict(first_name='Sandra', last_name='Jane', age=25)
print(person2, type(person2))

#Get Value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['height'] =  134
print(person)

# Get keys
print(person.keys())

# get items
print(person.items())

# copy dict
person3 = person.copy()
person3['first_name'] = 'James'
person3['town'] = 'Jinja'
print(person3)

# remove item
del person3['age']
print(person3)
del(person3['town'])
print(person3)
person3.pop('height')
print(person3)


# Clear
person3.clear()
print(person3)

# get length
print(len(person3))

# list of dict
people = [
    {'name':'Martha','age':25},
    {'name':'Thomas','age':35},
    {'name':'Claire','age':15},
]
print(people)
print(people[2]['age'])
