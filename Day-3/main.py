# Example 1
# So you have a bathtub in your bathroom with a depth if 90cm
# But youd'd love to have a stop measure to stop the water from overflowinf right?
# Here is somthing you can do about it with python

water_level = 80
if water_level < 80:
    print('Water is running')
else:
    print("Stop Water")


# Example 2
# So you working at a ticket store, and asked to write a code to sell tickets for a costaride
# If the height is 120cm or higher sell tickets, else don't seell
# If they can ride, check for age to determine how much will be the fare charge.
# Age 18 and above will pay $12 while age under 18 will pay $ 12
# Adding more conditions
# IF age is less than 12 pay $5
# If age is between 12 - 18 pay $7
# If age is above 18 pay $12
# If they want to take a picture, regardless of thier age add $3
# No ticket payment for people with mid life crises


height = int(input("What's your height in cm? "))
bill = 0

if height >= 120:
    print('You can ride the rollercoaster!')
    age = int(input("What your age? "))
    if age > 18:
        bill = 12
        print("Please pay $12.")
    elif age >= 12:
        bill = 7
        print("Please pay $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok, have a free ride on us!")
    else:
        bill = 5
        print("Please pay $5.")
    
    wants_photo = input("Do you wnat a photo take? Y or N")
    if wants_photo == "Y":
        bill +=3

    print(f"Your final bill is {bill}")
else:
    print('Sorry, you have to grow taller in order to ride.')

# Exercise 1
#Write a program that works out whether if a given number is an odd or even number.
#Even numbers can be divided by 2 with no remainder.

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


# Exercise 2
# Write a program that interprets the Body Mass Index(BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.


height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


new_height = float(height ** 2)
bmi = round(weight / new_height)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


# Excercise 3
# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.

# This is how you work out whether if a particular year is a leap year.

# on every year that is evenly divisible by 4 

# except every year that is evenly divisible by 100 

# unless the year is also evenly divisible by 400


year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400:
            print("Leap year.")

        else:
            print("Not leap year.")

    else:
        print("Leap year.")
else:
    print("Not leap year.")

# Check out this treasure island game out
# https://replit.com/@Olusegun-Light/treasure-island-start#main.py
