# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# Single Assignment
x = 1             # int
y = 2.5           # float
name = 'James'    # str 
is_cool = True    # bool

# Multiple assignemnt
_x, _y, _name, _is_cool = (1, 2.5, 'Jimmy', False)


# Casting
print(type(y))
y = str(y)
print(type(y))

# be careful of loss of precision when casting between float and int
y = float(y)
print(type(y), y)
y = int(y)
print(type(y), y)