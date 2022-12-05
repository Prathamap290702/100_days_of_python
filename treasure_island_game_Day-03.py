# if__else\
# odd or even

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
#         bill = 5
#         print("Child ticket is $5.")
#     elif age <= 18:
#         bill = 7
#         print("Teenager ticket is $7.")
#     else:
#         bill = 12
#         print("Adult ticket is $12.")
#     ch = input("Do you want your Photo taken for only $3?? Y/N : ")
#     if ch == 'Y':
#         bill +=3
#     else:
#       pass
#     print(f"You have to pay ${bill}.")

# BMI 2.0
# height = float(input("What is your height in metres : "))
# weight = float(input("What is your weight in kgs : "))
# print(type(height))
# bmi = float(weight) / float(height ** 2)
# print("Your BMI is : " + str(bmi))
# if bmi < 18.5:
#     print("You are Underweight Category.")
# elif bmi < 25:
#     print("You are in Ideal weight Category.")

# elif bmi < 30:
#     print("You are in Overweight Category.")
# elif bmi < 35:
#     print("You are in Obese Category")
# # else :
# #     print("You are Clinically Obese.")

# Leap Year
# year = int(input("Enter the year you want to check leap year : "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap Year.")
#         else:
#             print("Not a Leap Year.")
#     else:
#         print("Leap Year.")
# else:
#     print("Not a Leap Year.")

# if year % 400 == 0:
#             print("Leap Year.")

# PIZZA

# print("Welcome to the Python Pizza Deliveries 😄")
# size = input('''Which size of pizza do you want to try today?
# S - Small pizza  - $ 15
# M - Medium pizza - $ 20
# L - Large  Pizza - $ 25
# ''')
# pepp = input('''Do you want Pepperoni for your Pizza
# Pepperoni for Small Pizza  - $2
# Pepperoni for Medium Pizza - $3
# Pepperoni for Large Pizza  - $5
# (Y/N) :''')

# if size == 'S':
#     bill = 15
#     if pepp == 'Y':
#         bill+=2
# elif size == 'M':
#     bill = 20
#     if pepp == 'Y':
#         bill+=3
# elif size == 'L':
#     bill = 25
#     if pepp == 'Y':
#         bill+=5
# ches = input("Do you want Extra Cheese on your Pizza for just $1 (Y/N) : ")
# if ches == 'Y':
#     bill+=1
# print(f"Total Bill = ${bill} \n Please visit again 😁 and have a nice day.")

# Love Calculator
# print("Welcome to love calculator")
# name1 = input("Enter your name : ")
# name2 = input("Enter their name : ")
# name1 = name1.lower()
# name2 = name2.lower()
# C1 = name1.count('t') + name2.count('t')
# C2 = name1.count('r') + name2.count('r')
# C3 = name1.count('u') + name2.count('u')
# C4 = name1.count('e') + name2.count('e')
# count1 = C1 + C2 + C3 + C4
# C5 = name1.count('l') + name2.count('l')
# C6 = name1.count('o') + name2.count('o')
# C7 = name1.count('v') + name2.count('v')
# C8 = name1.count('e') + name2.count('e')
# count2 = C5 + C6 + C7 + C8    
# print("Your Love Percentage is " + str(count1)+str(count2) + "%")

# Treasure Island
print('''                                    o
                                   $""$o
                                  $"  $$
                                   $$$$
                                   o "$o
                                  o"  "$
             oo"$$$"  oo$"$ooo   o$    "$    ooo"$oo  $$$"o
o o o o    oo"  o"      "o    $$o$"     o o$""  o$      "$  "oo   o o o o
"$o   ""$$$"   $$         $      "   o   ""    o"         $   "o$$"    o$$
  ""o       o  $          $"       $$$$$       o          $  ooo     o""
     "o   $$$$o $o       o$        $$$$$"       $o        " $$$$   o"
      ""o $$$$o  oo o  o$"         $$$$$"        "o o o o"  "$$$  $
        "" "$"     """""            ""$"            """      """ "
         "oooooooooooooooooooooooooooooooooooooooooooooooooooooo$
          "$$$$"$$$$" $$$$$$$"$$$$$$ " "$$$$$"$$$$$$"  $$$""$$$$
           $$$oo$$$$   $$$$$$o$$$$$$o" $$$$$$$$$$$$$$ o$$$$o$$$"
           $"""""""""""""""""""""""""""""""""""""""""""""""""""$
           $"                                                 "$
           $"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$
''')