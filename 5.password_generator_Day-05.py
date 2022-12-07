# loops
# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#     print(fruit)
#     print(fruit + "pie")


# Avg height
# students_height = input("Input the list of student heights : ").split()
# print(students_height)
# sum = 0
# for height in students_height:
#     sum += int(height)
# print(round(sum/len(students_height), 2))

# highest score
# scores = input("Input all the scores : ").split()
# print(scores)
# max = 0
# for score in scores:
#     if int(score) >= int(max):
#         max = score
# print(max)

# range
# for number in range(0, 101, 5):
#     print(number)

# sum of even numbers
# total = 0
# for num in range(2, 101, 2):
#     total += num
#     print(num)
# print(total)

#fizz and buzz
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


# Password Generator
import string
import random
letters = list(string.ascii_letters)
numbers = list(range(0, 10))
symbols = ['~', ':', "'", '+', '[', '\\', '@', '^',
           '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

print("Welcome to the Pypassword Generator :) ")
letter = int(input("How many letters would you like in your password : "))
symbol = int(input("How many symbols would you like in your password : "))
num = int(input("How many numbers would you like in your password : "))
passs = []
for char in range(letter):
    random_char = random.choice(letters)
    passs += random_char
for int in range(num):
    random_num = random.choice(numbers)
    passs += str(random_num)
for sym in range(symbol):
    random_sym = random.choice(symbols)
    passs += str(random_sym)
# old  way
# password = ""
# for p in range(len(passs)):
#     random_pass = random.choice(passs)
#     password += random_pass
# print(f"Here is your password : {password}")

# easy way
password = ""
for p in range(len(passs)):
    password += str(p)
random.shuffle(passs)
password_final = ""
for p in passs:
    password_final += str(p)
print(password_final)
