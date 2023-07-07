#  Read File
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

#  Write to a file
with open("my_file.txt", mode="w") as file:
    file.write("New Text")

#  Append new words to a file
with open("my_file.txt", mode="a") as file:
    file.write("\nNew Text 2")

#  Work using file paths
with open("../my_files.txt") as file:
    file.write("New file path")
