# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# sample JSON
userJSON = '{"first_name":"John", "age":30}'

# parse to dict
user = json.loads(userJSON)

print(type(userJSON))
print(type(user))
print(user)


car = {"make":"Toyota", "model":"corolla","year":1998}
carJSON = json.dumps(car)
print(carJSON)

