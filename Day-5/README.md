# Python Loops

This repository contains Python code examples and explanations related to loops in Python. It explores the use of for loops, range() function, and various loop scenarios.

## For Loops

A for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects. Here are some examples of using for loops:

```python
for item in list_of_items:
    # Do something with each item
```

- Loops help execute the same line of code multiple times, allowing you to perform repetitive tasks efficiently.

## Range() Function

The `range()` function is often used in conjunction with for loops to generate a sequence of numbers. Here are some examples of using the `range()` function in for loops:

```python
# Loop from a to b (exclusive)
for number in range(a, b):
    print(number)

# Loop from 1 to 10 (inclusive)
for number in range(1, 11):
    print(number)

# Loop with a step size of 3
for number in range(1, 11, 3):
    print(number)
```

- By default, the `range()` function steps through all the values from the start to the end, increasing by 1. However, you can specify a different step size if needed.

## Loop Examples

The provided code includes several examples of different loop scenarios:

1. Calculating the Average Height of Students:

   - Takes input of a list of student heights and calculates the average height using a for loop, the `split()` method, and the `int()` function.

2. Finding the Highest Number in a List:

   - Takes input of a list of student scores and finds the highest score using a for loop, the 'split()' method, and comparison operators.

3. Adding Up Numbers:

   - Adds up all the numbers from 1 to 100 using a for loop and a running total.

4. Sum of Even Numbers:

   - Calculates the sum of all even numbers from 1 to 100 using two different approaches: one with a step size of 2 and the other with an if condition.

5. Fizz Buzz Game:
   - Prints numbers from 1 to 100, replacing multiples of 3 with "Fizz," multiples of 5 with "Buzz," and multiples of both 3 and 5 with "FizzBuzz."

Feel free to explore the provided code examples and modify them to experiment with different scenarios!

## Getting Started

To run the code examples and try out different loop scenarios in Python, you need a Python environment set up on your machine. You can use an integrated development environment (IDE) or a text editor to write and execute the code. Make sure you have Python installed on your system.

1. Clone or download this repository to your local machine.
2. Open the code files in your preferred Python editor.
3. Run the code to see the output or modify it to experiment with different scenarios.
4. Feel free to explore and enhance your understanding of loops in Python!

## Resources

If you're new to loops or want to learn more about different loop scenarios in Python, consider checking out the following resources:

- [Python Documentation: for Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Real Python: Python For Loops: A Guide to Definite Iteration](https://realpython.com/python-for-loop/)
- [W3Schools: Python For Loops](https://www.w3schools.com/python/python_for_loops.asp)

Enjoy exploring the world of loops in Python!
