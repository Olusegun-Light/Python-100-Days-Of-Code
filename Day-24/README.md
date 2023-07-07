# File Operations

This Python code demonstrates various file operations, including reading from and writing to files, as well as appending content and working with file paths.

## Reading from a File

To read the contents of a file, you can use the `open()` function with the file name and the mode set to `"r"` (read). The `with` statement ensures that the file is properly closed after reading.

```python
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
```

### Writing to a File

To write content to a file, you can use the `open()` function with the file name and the mode set to `"w"` (write). The `with` statement ensures that the file is properly closed after writing.

```python
with open("my_file.txt", mode="w") as file:
    file.write("New Text")
```

### Appending to a File

To append content to an existing file, you can use the `open()` function with the file name and the mode set to `"a"` (append). The `with` statement ensures that the file is properly closed after appending.

```python
with open("my_file.txt", mode="a") as file:
    file.write("\nNew Text 2")
```

### Working with File Paths

You can also work with file paths to read or write files in different directories. Simply provide the file path as the argument to the `open()` function.

```python
with open("../my_files.txt") as file:
    file.write("New file path")
```

Please note that proper file permissions are required for reading from or writing to files. Ensure that you have the necessary permissions to perform the desired file operations.
