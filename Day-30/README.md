# Errors and Exceptions

This Python script exemplifies error and exception handling through various scenarios:

## File Handling

The script aims to open a file named "a_file.txt". If the file is not found, it creates the file and writes the text "Something" into it. The script handles exceptions including `FileNotFoundError` and `KeyError`, providing informative error messages.

    ```python
    try:
        file = open("a_file.txt")
        a_dictionary = {"key": "value"}
    except FileNotFoundError:
        file = open("a_file.text", 'w')
        file.write("Something")
    except KeyError as error_message:
        print(f"The key {error_message} does not exist")
    else:
        content = file.read()
        print(content)
    finally:
        raise KeyError
    ```

## Input Validation

The script prompts for height and weight inputs and calculates the BMI (Body Mass Index). It uses a ValueError exception to prevent unrealistic human heights exceeding 3 meters.

    ```python
        height = float(input("Height: "))
        weight = float(input("Weight: "))

        if height > 3:
            raise ValueError("Human Height should not exceed 3 meters")
        bmi = weight / height ** 2
        print(bmi)
    ```

This code showcases the utilization of `try`, `except`, `else`, and `finally` blocks to gracefully manage different types of exceptions and errors. It underscores the importance of error handling for ensuring the stability of code execution.
