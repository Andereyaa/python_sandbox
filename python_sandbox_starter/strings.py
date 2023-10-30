# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods


name = 'Brad'
age = 57

# Concatenate
print('Hello, ny name is '+ name + ' and I am ' + str(age))


# String Formatting


# Arguments by position
print('My name is {name} and i am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
print(f'Hello, my name is {name} and I am {age}')


# String Methods

s = 'Hello World'

# String Operations
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(len(s))
print(s.replace('world','everyone'))
print(s.startswith('hello'))
print(s.endswith('d'))
print(s.split())
print(s.isalnum())
print(s.isalpha())
print(s.isnumeric())
