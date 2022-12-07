import random
# random_integer = random.randint(100, 200)
# random_flaot = random.random()
# print(random_integer)
# print(random_flaot)

# Toss
# random_integer = random.randint(0, 1)
# if random_integer == 1:
#     print("Heads")
# else :
#     print("Tails")

# lists are just like arrays
# my_list = ['h', 'he', 'li', 'be', "b", 'c', 'n', 'o', 'f', 'ne']
# # print(my_list)
# my_list.append('na')
# my_list.extend(['mg', 'al', 'si'])
# print(my_list)

# who will pay the bill
# names_in = input("Enter the name of all the diners separated by a comma : ")
# names = names_in.split(", ")
# print(names)
# rand = random.randint(0, len(names) - 1)
# print(f"{names[rand]} will pay the bill today.")

# person_who_will_pay = random.choice(names)// more easy way to write the code
# print(f"{person_who_will_pay} will pay the bill today.")

# nested lists
# num = [1,2,3,4,5]
# alphabets = [ 'a', 'b', 'c', 'd', 'e']
# alphanumerics = [num,alphabets]
# print(alphanumerics)

# treasure
# row1 = ['🥲', '🥲', '🥲']
# row2 = ['🥲', '🥲', '🥲']
# row3 = ['🥲', '🥲', '🥲']
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Enter the position you want to bury the treasure : ")
# horizontal = int(position[0])
# vertical = int(position[1])
# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] ="😁"
# print(f"{row1}\n{row2}\n{row3}")
# Rock Paper Scissors ASCII Art

# Rock
stone = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
your_choice = int(input("Choose 0 / 1 / 2 for stone / paper / scissors :"))
choice = random.randint(0, 2)
print("You : ")
if your_choice == 0:
    print(stone)
elif your_choice == 1:
    print(paper)
elif your_choice == 2:
    print(scissors)

print("Computer : ")
if choice == 0:
    print(stone)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
    
if your_choice - choice == 1 or your_choice - choice == -2:
    print("You Win!!!")
elif choice - your_choice == 1 or your_choice - choice == 2:
    print("You Lose...")
elif your_choice == choice:
    print("Tie")
