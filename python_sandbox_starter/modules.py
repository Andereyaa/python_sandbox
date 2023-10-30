# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

import datetime
from datetime import date
import time

# today = datetime.date.today()
today = date.today()
timestamp = time.time()

print(today)
print(timestamp)

# pip module
from camelcase import CamelCase

c = CamelCase()
print(c.hump('hello there world'))

# import custom module
from validator import validate_email
email = 'test@test.com'

if validate_email(email=email):
    print('email is valid')
else:
    print('email is bad')