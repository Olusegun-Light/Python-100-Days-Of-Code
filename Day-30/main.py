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

height = float(input("Height: "))
weight = float(input("Weight: "))


if height > 3:
    raise ValueError("Human Height should not be over 3 meters tall")
bmi = weight / height ** 2
print(bmi)
