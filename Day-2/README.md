# Understanding Data Types and How to Manipulate Strings

## Data Types

1. Integer: Whole number positive or negative, numbers without decimal places
    To declare an integer, unlike string needing the double quotes you just write the numbers.
    Example 123, 3490

    - Sub-scripting is a method of pulling a perticular element from a string
        Example; If you have a string "Hello" you can get any element from the string

        ```
        print('Hello'[0])

        >H
        ```

        ```
        print('Hello'[-1])

        >0
        ```

2. Float: They are numbers with decimal places also called floating point number.
    Example 3.12 9.8

3. Boolen: It has only two possiple values. True or False

4. Type checking: Use the type() function to know what type of data
    - Type conversion/Casting: Change one perticular data type to another
    -type() used to check the type of data
    - str() to convert to a string
    - int() to convert to an integer, and so one....

5. Mathimatical symbols
    Addition +
    Subtraction -
    Multiplication *
    Division / -float
    Floor Division // -int
    Exponent **

    - Round numbers to the nearest whole number with round() function

    - F-Strings: new string formatting mechanism known as Literal String Interpolation. The idea behind f-strings is to make string interpolation simpler. 
        - To implement it you fut an f infront of the string

        ```
        score = 0 
        height = 1.8
        isWinning = True
        print(f"your score is {score}, your height is {height} and the probability of you winning is {isWinning}" )
        ``` 