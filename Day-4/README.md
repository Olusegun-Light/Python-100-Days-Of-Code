# Randomalising Python

1. Randomization
    - Pusdo random number generator, python uses the [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister) to generate random numbers.

    - Generate random whole number 
        randint(a, b) -> Returns a random integer between a and b (both inclusive). This also raises a ValueError if a > b.

    - Generate random floating point number
        random.random() -> Returns the next random floating point number between [0.0 to 1.0]


2. Module is a file containing Python code, definitions of functions, statements, or classes.
    - You can create your own module by creating a new py file, defining your functions/statement then import it where neccesarry

3. Lists: This what you call a Data Structure. It a way of organizing and storing data. List is used to store grouped peice of data

        ```
        fruits = ["item1", "item2", "item3"]
        ```
        - The data stored in the list are in order. Counting starts from 0

        - Use .len() to check the number of items in the list
        - Use .append() to add a single item to the end of the list
        - Use .extend() tp add multiple items to the list
        - More list methods [here](https://www.w3schools.com/python/python_lists_add.asp).
    
    - Nested List: a combination of two diffrent list to one
        
        ```
        fruits = ["dbfjksd", "fjskd", "uewht"]
        vegetables = ["potato", "tomato", "onion"]

        dirty_dozen = [fruits, vegtables]
        ```
        
