# function
# def my_function():
#     print("hello")
#     print("Bye")
# my_function()

# reeborg's world
# code there
# def turn_around():
#     turn_left()
#     turn_left()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# for step in range(5):
#     jump()

# while
# while hurdles > 0:
#     jump()
#     hurdles -= 1

# hurde 2 random goal placement
# while at_goal()!=True:
#     jump()



# hurdle 3 random wall placement


# def turn_around():
#     turn_left()
#     turn_left()
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# for step in range(6):
#    jump()
# while at_goal()!=True:
#   jump()
# while at_goal()!=True:
#     if front_is_clear() != False:
#         move()
#     if wall_in_front() == True:
#         jump()



#Hurdles4 Variable height of the wall
# def turn_around():
#     turn_left()
#     turn_left()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while wall_in_front() != True:
#         move()
#     turn_left()
# while at_goal()!=True:
#     if wall_in_front():
#         jump()
#     else:
#         move()


#escape the maze 
# def turn_around():
#     turn_left()
#     turn_left()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while at_goal() != True:
#     if front_is_clear() == True and right_is_clear() == True:
#         turn_right()
#         move()
#     elif front_is_clear() == True and right_is_clear() != True:
#         move()
#     elif front_is_clear() != True and right_is_clear() == True:
#         turn_right()
#         move()
#     elif front_is_clear() != True and right_is_clear() != True:
#         turn_left()