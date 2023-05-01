print(123 + 567)

num_char = len(input("What's ypur name?"))
new_num_char = str(num_char)
print("your name has" + new_num_char + " characters.")

#f-string
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height} and the probability of you winning is {isWinning}")

# Excercise 
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
# Tip Calculator

print("Welcome to tip Calculator")
total_bill = float(input("What was the total bill? $"))
percentage_tip = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
num_of_people = int(input("How many people will split the bill? "))
tip = total_bill * (percentage_tip/100)
new_total = total_bill + tip
split_bill = new_total / num_of_people
split_bill_dec = round(split_bill, 2)
print(f"Each person should pay: {split_bill_dec}")
