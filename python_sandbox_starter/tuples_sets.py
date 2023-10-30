# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create Tuple
fruits = ('apple', 'bananas', 'carrots', 'jackfruit', 'soursop', 'mangoes')
# fruits2 = tuple(('apple', 'bananas', 'carrots', 'jackfruit', 'soursop', 'mangoes'))

fruits2 = ('applies')
print(fruits2, type(fruits2))

# single value needs trailing comma
fruits2 = ('applies',)
print(fruits2, type(fruits2))


# Get value
print(fruits[1])

# Can't change value
# fruits[0] = 'Promengranate'
# del fruits[1]
print(fruits)
 


# A Set is a collection which is unordered and unindexed. No duplicate members.

# creation
colors = {'red', 'pink', 'purple', 'blue', 'orange'}
colors2 = set(('red', 'pink', 'purple', 'blue', 'orange'))

print(colors2, type(colors2))

# check if in set
print('pink' in colors)

# add to set
colors.add('green')
print(colors)

# remove from set
colors.add('purple')
print(colors)

# clear set
colors.clear()
print(colors)