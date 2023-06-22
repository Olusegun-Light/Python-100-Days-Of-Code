# Understanding Data Types and How to Manipulate Strings

This README provides an overview of data types in Python and covers concepts such as integers, floats, booleans, type checking, type conversion, mathematical symbols, and f-strings. It also includes an exercise example of a Tip Calculator.

## Data Types

1. Integer: Integer represents whole numbers, either positive or negative, without decimal places.

Example:

```
123
3490
```

- Subscripting: Subscripting is a method of accessing a particular element from a string. You can use square brackets `[]` with the index position to retrieve a specific element.

Example:

```python
print('Hello'[0])
# Output: H

print('Hello'[-1])
# Output: o
```

2. Float: Float represents numbers with decimal places, also known as floating-point numbers.

Example:

```
3.12
9.8
```

3. Boolean: Boolean has only two possible values: `True` or `False`.

4. Type Checking and Type Conversion (Casting):

- Use the `type()` function to check the type of data.
- Use `str()` to convert to a string.
- Use `int()` to convert to an integer, and so on.

5. Mathematical Symbols:

- Addition: `+`

- Subtraction: `-`

- Multiplication: `*`

- Division: `/` (float division)

- Floor Division: `//` (integer division)

- Exponent: `**`

- Rounding Numbers: Use the `round()` function to round numbers to the nearest whole number.

- F-Strings (Literal String Interpolation): F-strings provide a simpler way to format strings by embedding expressions inside string literals. To use f-strings, prefix the string with the letter `f` and enclose expressions within curly braces `{}`.

Example:

```python
score = 0
height = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height}, and the probability of you winning is {isWinning}")
```

## Exercise: Tip Calculator

This exercise demonstrates the usage of the concepts mentioned above. It calculates the amount each person should pay, including the tip, when splitting a bill among multiple people.

Example:

```python
print("Welcome to the Tip Calculator")

total_bill = float(input("What was the total bill? $"))
percentage_tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people will split the bill? "))

tip = total_bill * (percentage_tip / 100)
new_total = total_bill + tip
split_bill = new_total / num_of_people
split_bill_dec = round(split_bill, 2)

print(f"Each person should pay: {split_bill_dec}")
```

This code snippet prompts the user for the total bill, the percentage tip, and the number of people splitting the bill. It calculates the tip, adds it to the total bill, and divides the new total among the specified number of people. The final amount each person should pay is displayed.

# Conclusion

This README provides an understanding of data types in Python, including integers, floats, and booleans. It also covers type checking, type conversion, mathematical symbols, and f-strings for string formatting. Feel free to modify and experiment with the code examples to explore different functionalities.

If you have any questions or encounter any issues, please feel free to reach out.

Happy coding!
