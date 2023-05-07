
fruits = ["apple", "peach", "pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# Range in loop
for number in range(1, 10):
    print(number)

# Increase step
for number in range(1, 11, 3):
    print(number)

# Calculating the the average height of students

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


# Sum() Function
total_height = 0
for height in student_heights:
    total_height += height
# print(total_height)

# Len() function
number_of_students = 0
for student in student_heights:
    number_of_students += 1
# print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)



# Get the highest number in a list

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")


# Add up all the numbers from 1 to 100
total = 0 
for number in range(1, 101):
    total += number
    print(total)

# A program that calculates the sum of all the even numbers from 1 to 100
# There are two approch to this 
# 1 Using step size

total = 0
for number in range(2, 101, 2):
    total += number
print(total)

# 2  

total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)

# Fizz Buzz Game
# Write a program that prints the numbers from 1 to 100. For multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For multiples of three and five print "FizzBuzz"


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
