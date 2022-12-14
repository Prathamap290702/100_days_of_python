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

#Number Guessing game: