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
two_digit = input("Enter a two digit number : ")
# print(type(two_digit))
# unit = int(two_digit % 10)
# ten = int(two_digit / 10)
# print(unit + ten)
first = two_digit[0]
second = two_digit[1]
print(int(first) + int(second))