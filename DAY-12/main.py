####### Scope #########

enemies = 1

def increase_enimies():
    enemies = 2
    print(f"enimies inside function: {enemies}")

increase_enimies()
print(f"enimies outside function: {enemies}")

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength) ####will give an error, potion_strength not defined

# Global Scope

player_heath = 10

def drink_potion():
    potion_strength = 2
    print(player_heath)


drink_potion()

# Modifying Global Scope

enemies = 1

def increase_enimies():
    print(f"enimies inside function: {enemies}")
    return enemies + 2

enimies = increase_enimies()
print(f"enimies outside function: {enemies}")

# Global Constants
PI = 3.14259
GIT_HUB_USER_NAME = "Olusegun Light"
