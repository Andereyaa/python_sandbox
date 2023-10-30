# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    def has_birthday(self):
            self.age += 1
        
# init user object
brad = User('Brad Traversy', 'brad@traversy.com', 13)

print(type(brad))
print(brad.age)
print(brad.has_birthday())
print(brad.greeting())

# Extend class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
        
    def set_balance(self, balance):
        self.balance = balance
        
    def greeting(self):
        print(super().greeting())
        return f'My name is {self.name}. I am {self.age} and my balance is {self.balance}'
    
        
# init customer objct
janet = Customer('Janet', 'janet@gmail.com', 35)
janet.set_balance(1000)
print(janet.greeting())