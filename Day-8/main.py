def greet():
    print("hello")
    print("world")
    print("hello word")

greet()

# Function that allows for input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Light")

def greet_with_name2(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

name = input("What's your name?")
             
greet_with_name2(name)

#Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello may name is {name}, currently based at {location}")
user_name = input("What's your name? " )
user_address = input("Where's your current location? ")
greet_with(user_name, user_address )

# Functions with keyword arguments
# To avoid positional arguments we map each function name
greet_with(location=user_address, name=user_name)





