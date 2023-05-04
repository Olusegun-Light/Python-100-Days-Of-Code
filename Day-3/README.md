# Control Flow and Logical Operators

1. Conditional statement
    - if else statement

        ```
        if condition:
            do this
        else:
            do this
        ```

        Lets use our bathtub water level for example

        ```
        water_level = 50 
        if water_level > 80:
            print("Drain water!")
        else:
            print("Continue filling")
        ```
    
    - Nested if/else statement
    
        ```
        if condition:
            if another condition:
                do this
            else:
                do this
        else:
            do this
        ```
    - if / elif / else statement

        ```
        if condition1:  
            do A
        elif condition2:
            do B
        else: do this
        ```

        - You can add as many elif statement 

    - Multiple if

    ```
        if condition1:  
            do A
        if condition2:
            do B
        if: condition3:
            do C
        ```


2. Comparison Operators
    | Operator      | Meaning                  |
    | :---          |    :----:                |
    | >             | Greater than             |
    | <             | Less than                |
    | >=            | Greater than or equal to |
    | <=            | Less than or equal to    |
    | ==            | Equal to                 |
    | !=            | Not equal to             |

    More on *[Comparison Operators](https://www.w3schools.com/python/gloss_python_comparison_operators.asp)*.

    - *Note*: The equal sign might be a bit tricky or confusing for beginners. The single equal sign "=" is used to asign a value to a varaible, while the double equal sign "==" is used to  check a condiiton.


3. Logical Operators 
    - and
    - or 
    - not 