# if__else\
#odd or even

# num = int(input("Enter the number you want to check odd or even : "))
# if num%2==0:
#     print(f"{num} is Even.")
# else:
#     print(f"{num} is Odd.")

# print("Welcome to the Rollercoaster ride")
# height = int(input("What is your height in cms : "))
# age = int(input("What is your age : "))
# if height < 120:
#     print("You cannot ride the Rollercoaster.")
# else:
#     print("You can ride the Rollercoaster.")
#     if age<12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")

# BMI 2.0
height = float(input("What is your height in metres : "))
weight = float(input("What is your weight in kgs : "))
print(type(height))
bmi = float(weight) / float(height ** 2)
print("Your BMI is : " + str(bmi))
if bmi < 18.5:
    print("You are Underweight Category.")
elif bmi < 25:
    print("You are in Ideal weight Category.")

elif bmi < 30:
    print("You are in Overweight Category.")
elif bmi < 35:
    print("You are in Obese Category")
else :
    print("You are Clinically Obese.")