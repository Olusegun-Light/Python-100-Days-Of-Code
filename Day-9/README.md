# Dictionaries, Nesting, and the Secret Auction

## 1. Dictionaries

Dictionaries in Python allow us to group and tag related pieces of information together. They are represented by key-value pairs. Here's an example of a dictionary:

```python
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something repeatedly."
}
```

We can access the values in the dictionary using the keys. For example:

```python
print(programming_dictionary["Bug"])
```

This will print the value associated with the key "Bug".

## 2. Adding and Editing Dictionary Items

We can add new items to a dictionary by assigning a value to a new key, like this:

```python
programming_dictionary["Loop"] = "The action of doing something repeatedly."
```

To edit an existing item in the dictionary, we can simply reassign a new value to the desired key:

```python
programming_dictionary["Bug"] = "A moth in your computer"
```

## 3. Looping through a Dictionary

We can loop through a dictionary using a for loop. This allows us to access both the keys and values of the dictionary:

```python
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
```

## 4. Nesting in Dictionaries

Dictionaries can be nested inside other dictionaries or other data types like lists. This allows us to create more complex data structures. Here are some examples:

- Nesting a List in a Dictionary:

```python
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}
```

- Nesting a Dictionary in a Dictionary:

```python
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 11
    }
}
```

- Nesting a Dictionary in a List:

```python
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 9
    }
]
```

Feel free to adjust the formatting and content as needed.

### Happy Learning!!
