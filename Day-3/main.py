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

height = int(input("What's your height in cm? "))

if height >= 120:
    print('You can ride the rollercoaster!')
else:
    print('Sorry, you have to grow taller in order to ride.')

# Exercise
#Write a program that works out whether if a given number is an odd or even number.
#Even numbers can be divided by 2 with no remainder.

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

