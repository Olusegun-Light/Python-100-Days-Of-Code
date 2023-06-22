# Scope & Number Guessing Game

This module explores the concept of scope in Python and provides an example of a Number Guessing Game.

## Scope Overview

1.  **Local Scope** : Variables defined within a function are accessible only inside that function. They are not accessible outside the function.

Example:

```python
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
```

2. **Global Scope**: Variables defined at the top level of a file are accessible globally throughout the program.

Example:

```python
enemies = 1

def increase_enemies():
    global enemies
    enemies += 2
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")
```

3. **Block Scope**: Unlike some other programming languages, Python does not have block scope. Variables defined within loops or if statements are still accessible outside of them.

4. **Modifying Global Scope**: To modify a global variable within a function, you need to use the `global` keyword or return the modified value and assign it to the global variable.

Example:

```python
enemies = 1

def increase_enemies():
    global enemies
    enemies += 2
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")
```

5. **Global Constants**: Constants are variables that are not meant to be changed. In Python, they are typically named in uppercase to indicate their constant nature.

Example:

```python
PI = 3.14259
GITHUB_USERNAME = "Olusegun Light"
```

## Number Guessing Game

The Number Guessing Game is an interactive game where the player tries to guess a random number chosen by the computer. The game provides feedback on whether the guess is too high or too low until the player guesses the correct number.

## How to Play

1. The computer selects a random number between 1 and 100.
2. The player is prompted to guess a number.
3. The game provides feedback on whether the guess is too high or too low.
4. The player continues guessing until the correct number is guessed.
5. The game displays the number of attempts taken to guess correctly.

Enjoy playing the Number Guessing Game and have fun!
