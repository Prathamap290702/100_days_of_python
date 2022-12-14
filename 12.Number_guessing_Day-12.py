# Scope

# enemies = 1


# def increase_enemies():
#     enemies = 2
#     print(f"Enemies inside the function are {enemies}")


# increase_enemies()
# print(f"Enemies outside the function are {enemies}")

# Local scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strenght) # this is wrong as it was not outside the function

# Global scope
# player_health = 10


# def game():
#  def drink_potion():
#      potion_strength = 2
#      print(player_health)

#  drink_potion()
# print(player_health)

# There is no block
# game_level = 3


# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level<5:
#         new_enemy = enemies[0]

#     print(new_enemy)
# create_enemy()

# modifying global variable
# use global before the varible name
# enemies = 1

# def xyz():
#     global enemies
#     enemies = 2

# xyz()
# print(enemies)

# Global constants
# all upper case
# PI = 3.14
# URL = "https://www.google.com"


# Number Guessing game:
import random
lives = 0


def game(lives):
    num = random.randint(1, 101)
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess : "))
        if num > guess:
            print("Too low.")
        elif num < guess:
            print("Too high.")
        elif num == guess:
            print(f"You got it! The answer was {guess}.")
            return
        lives -= 1
    if lives == 0:
        print("You ran out of guesses, You lose.")


print("Welcome to the Number Guessing game!")
level = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
if level == 'easy':
    lives = 10
    game(lives)
else:
    lives = 5
    game(lives)
