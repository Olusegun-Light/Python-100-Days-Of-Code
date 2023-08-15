# List and Dictionary Comprehensions in Python

This repository contains Python code examples demonstrating the use of list and dictionary comprehensions. Comprehensions are concise and powerful ways to create lists and dictionaries based on existing iterables. The provided code showcases various types of comprehensions and their applications.

## Code Examples

### For Loop and List Comprehension

1. **For Loop**: Using a traditional `for` loop to create a new list by adding 1 to each element in an existing list.

   ```python
   numbers = [1, 2, 3]
   new_list = []
   for n in numbers:
       add_1 = n + 1
       new_list.append(add_1)
   ```

2. **List Comprehension**: Achieving the same result using a list comprehension.

   ```python
   new_list = [n + 1 for n in numbers]
   ```

### String and Range Comprehension

3. **String as List**: Converting each character of a string into a list of letters.

   ```python
   name = "Angela"
   letters_list = [letter for letter in name]
   ```

4. **Range as List**: Creating a new list by doubling the values in a range.

   ```python
   range_list = [n * 2 for n in range(1, 5)]
   ```

### Conditional List Comprehension

5. **Conditional List Comprehension**: Selecting names from a list based on their length.

   ```python
   names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
   short_names = [name for name in names if len(name) < 5]
   upper_case_names = [name.upper() for name in names if len(name) > 4]
   ```

### Dictionary Comprehension

6. **Dictionary Comprehension**: Generating a dictionary of student grades using names as keys and random grades as values.

   ```python
   import random
   student_grades = {name: random.randint(1, 100) for name in names}
   print(student_grades)
   ```

7. **Conditional Dictionary Comprehension**: Creating a new dictionary containing only students who have passed (grades >= 60).

   ```python
   passed_students = {
       student: grade
       for (student, grade) in student_grades.items() if grade >= 60
   }
   print(passed_students)
   ```

## Usage

You can use these examples as a reference to understand and implement list and dictionary comprehensions in your Python projects. Feel free to modify and adapt the code snippets to suit your specific use cases.

List and dictionary comprehensions provide an elegant and efficient way to process and manipulate data in Python. They contribute to writing cleaner and more concise code. If you have any questions or want to explore more advanced use cases, please refer to the Python documentation or other learning resources.

Enjoy experimenting with list and dictionary comprehensions in your Python programming journey!
