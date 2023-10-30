# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['apples','bananas','mangos','oranges']

# use a constructor
numbers2 = list((1,2,3,4,5))

print(numbers, numbers2)

# Get a Value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('grapes')
print(fruits)

# Remove from list
fruits.remove('bananas')
print(fruits)

# insert into position
fruits.insert(1, 'guavaa')
print(fruits)

# Remove with pop
fruits.pop()
print(fruits)

# Change value
fruits[0] = 'jackfruit'
print(fruits)

# Reverse list
fruits.reverse()
print(fruits)

# Sort list
fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)