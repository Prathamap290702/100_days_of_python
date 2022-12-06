# Data types

# Strings
# print(len("Hello"))
# print("Hello"[1:      ])
# print("123" + "345")

# Integer
# print(123+345)
# 123_456_789 == 123456789

# float
# 3.14159
# Boolean
# True or False
# num_char = len(input("What is your name : "))
# new_num_char  =  str(num_char)
# print("Your name is of " + new_num_char + " charchters.")
# print(type(num_char))
# a = float(123)
# print(type(a))
# print(70 + float(100.5) + a)
# two_digit = input("Enter a two digit number : ")
# print(type(two_digit))
# unit = int(two_digit % 10)
# ten = int(two_digit / 10)
# print(unit + ten)
# first = two_digit[0]
# second = two_digit[1]
# print(int(first) + int(second))

# BMI CALCULATOR
# height = float(input("What is your height in metres : "))
# weight = float(input("What is your weight in kgs : "))
# print(type(height))
# bmi  = float(weight) / float(height ** 2)
# print("Your BMI is : " + str(bmi))

# print(round(8/3,3)) 
# print(8//3) # floor division

# f-strings 
# score = 1
# height = 1.72
# winning = True
# print(f"Your score is {score}, your height is {height} and you are winning is {winning}")

# your life in weeks
# age = input("What is your current age : ")
# expected_age = input("What is your expected age : ")
# age_remaining = int(expected_age) - int(age)
# no_of_days = age_remaining * 365 + (age_remaining//4)
# no_of_weeks = age_remaining * 52
# no_of_months = age_remaining * 12
# print(f"You have {no_of_days}days, {no_of_weeks}weeks and {no_of_months}months to live if you expect to live for {expected_age}years")


# TIP CALCULATOR
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill : ₹"))
perc = int(input("What percentage tip would you like to give ? 10, 12, or 15? :"))
tip = total_bill * perc / 100
total_people = int(input("How many people will split the bill : "))
each_bill =  round((total_bill + tip) / total_people,2)
print(f"Each person should pay:  ₹{each_bill}")
