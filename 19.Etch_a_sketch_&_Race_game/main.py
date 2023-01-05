from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(
    "make your bet", "Which turtle will win the race? Enter a color : ")
color = ["red", "violet", "blue", "green", "yellow", "orange"]
set = int(-100)
all_turtles = []
for colors in color:
    col = str(colors)
    colors = Turtle(shape="turtle")
    colors.color(col)
    colors.penup()
    set += 40
    colors.goto(-230, set)
    all_turtles.append(colors) 

if user_bet:
    race_on = True
kaun_jeeta = "" 
while race_on:
    for turtles in all_turtles:
        if turtles.xcor() >= 250:
            race_on = False
            kaun_jeeta = turtles.pencolor()
        rand_distance = random.randint(0, 10)
        turtles.forward(rand_distance)
        
if kaun_jeeta == user_bet:
    print(f"You Won...{kaun_jeeta} won the race.")
else:
    print(f"You lose..The Winner is {kaun_jeeta}.")
# tim.goto(x= -230, y = -100)
# def move_forward():x
#     tim.forward(10)
# def move_backward():
#     tim.backward(10)
# def move_left():
#     tim.left(5)
# def move_right():
#     tim.right(5)

# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.listen()
# screen.onkey(key = 'w', fun = move_forward)
# screen.onkey(key = 's', fun = move_backward)
# screen.onkey(key = 'a', fun = move_left)
# screen.onkey(key = 'd', fun = move_right)
# screen.onkey(clear, "c")
screen.exitonclick()
