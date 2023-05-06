# Tap into the random module
import random
 
# Import custom module
import my_module
print(my_module.pi)


# Generate random whole numbers between 1 to 10 including 1 and 10
random_integer = random.randint(1, 10)
print(random_integer)


# Generate random floating point number bwtween 0 and 1
random_float = random.random()
random_float *= 5 
print(random_float)


# A little toss a coin game. 
random_size = random.randint(0,1)
if random_size == 1:
    print("Heads")
else:
    print("Tails")


# Example of lists
states_of_america = ["Delware", "Pennsyvania"]

# Get items in the list by order of arrangement
print(states_of_america[0])

# You can also edit items in the list by their order
states_of_america[0] = "New-York"
print(states_of_america)

# You can add an item to the list 
states_of_america.append("LightLand")
print(states_of_america)

# Add multiple items to the list
states_of_america.extend(["New-Jersey", "New York", "New-Hampshire"])
print(states_of_america)


# Nested List 

fruits = ["dbfjksd", "fjskd", "uewht"]
vegetables = ["potato", "tomato", "onion"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)


# Check out rock papper siccors game
# https://replit.com/@Olusegun-Light/rock-paper-scissors
