# def greet():
#     name = input("What is your name : ")
#     print(f"Hello {name}.")
#     print("Welcome to this world.")
#     print("This is the greet function")
# greet()
# def greet_with_name(naam):
#     print(f"Hello {naam}.")
#     print("Welcome to this world.")
#     print("This is the greet function")

# greet_with_name("Pratham")

# Function with more than one input
# def greet_with(naam, patta): #positional argument
#     print(f"Hello {naam}.")
#     print("Welcome to this world.")
#     print(f"How was your journey from {patta}")

# greet_with("pratham", "kalyan")

# def greet_with(naam, patta): #keyword argument
#     print(f"Hello {naam}.")
#     print("Welcome to this world.")
#     print(f"How was your journey from {patta}")

# greet_with(naam = "pratham",patta = "kalyan")

# Area Calculation
# import math
# def area_calc(height, width, coverage):
#     Total_cans = math.ceil(height * width / coverage)
#     print(f"Total no of cans required to do the painting : {Total_cans}")

# def input_fun():
#     height = int(input("Enter the height of the wall : "))
#     width = int(input("Enter the width of the wall : "))
#     coverage = int(input("Enter the coverage of per can of color : "))
#     area_calc(height, width, coverage)

# input_fun()

# Prime Number
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime == True:
#         print(f"The number {number} is prime.")
#     else:
#         print(f"The number {number} is not prime.")


# num = int(input("Enter the number you want to check prime for : "))
# prime_checker(num)


# Ceasar Cipher
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def Caesar(text, pos, ):
    def encrypt(text, pos):
        cipher_text = ""
        for letters in text:
         if letters in alphabet:
            position = alphabet.index(letters)
            new_position = position + pos
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letters
        print(f"The encoded text is {cipher_text} ")

    def decrypt(text, pos):
        cipher_text = ""
        for letters in text:
            if letters in alphabet:
                position = alphabet.index(letters)
                new_position = position - pos
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            else:
                cipher_text += letters
        print(f"The decoded text is {cipher_text} ")

    if direction == "encode":
        encrypt(text, pos)
    elif direction == "decode":
        decrypt(text, pos)


loop = "y"
print(logo)
if loop == 'y':
    direction = input("Type 'encode' to encrypt, 'decode' to decrypt. ")
    text = input("Enter the message : ").lower()
    pos = int(input("Enter the number of positions to be shifted : "))
    if pos <= 25:
        Caesar(text, pos)
    else:
        print("Your shift position is too high.")
    loop = input("Do you want to continue (Y/N) : ").lower()
else:
    print("Goodbye....")
