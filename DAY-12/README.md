# Scope & Number Guessing Game

1. Local Scope exist within functions
   -When you create a new var or a new func inside another func it's only accessible inside that function

   ```
   def drink_potion():
   potion_strength = 2
   print(potion_strength)

   drink_potion()
   ```

2. Global scope

   - The difference between global scope and local scope is where you define or where you create your variables or your functions. Its available globally because it was defined at the top level of the file

   ```
   player_heath = 10

   def drink_potion():
       potion_strength = 2
       print(player_heath)


   drink_potion()
   ```

3. Block scope
   -There is no such thing as block scope in python.

4. Modifying global scope
   -Don't try to modify a global scope within a function that has a local scope

   ```
   enemies = 1

   def increase_enemies():
       global enemies
       enemies += 2
       print(f"enemies inside function: {enemies}")

   increase_enemies()
   print(f"enemies outside function: {enemies}")
   ```

   - Instead of modifying you can use the return statement

   ```
   enemies = 1

   def increase_enemies():
       print(f"enemies inside function: {enemies}")
       return enemies + 2

   enemies = increase_enemies()
   print(f"enemies outside function: {enemies}")

   ```

5. Global constants

   - Global constants are variable you define and never planning on changing it ever again
   - To differentiate it from regular function you change to name to all upper case

   ```
   PI = 3.14259
   GIT_HUB_USER_NAME = Olusegun Light
   ```
