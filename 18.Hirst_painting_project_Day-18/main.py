import turtle as t
import random
import colorgram
# import turtle
# tim = turtle.Turtle()//every time we have to write turtle.

# from turtle import * //import everything

# import turtle as t //alias

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colours = (r, g, b)
    return colours
# tim.forward(100)

# make square
# for i in range(0,4):
#     tim.forward(100)
#     tim.left(90)

# dashed lines
# for _ in range(0,15):
#     tim.forward(10)
#     tim.pu()
#     tim.forward(10)
#     tim.pd()

# drawing different shapes


# def draw(sides):
#     for i in range(0, sides):
#         tim.forward(100)
#         tim.left(360/sides)


# colors = ["medium orchid", "chartreuse", "cyan", "red", "blue",
#           "yellow", "deep sky blue", "dark violet", "aquamarine"]
# for i in range(3, 11):
#     tim.color(random.choice(colors))
#     draw(i)
direction = [0, 90, 180, 270]

# for i in range(0, 200):
#     tim.pensize(15)
#     tim.speed(10)
#     tim.color(random_color())
#     tim.forward(20)
#     tim.setheading(random.choice(direction))
#     # tim.forward(20)

tim.speed(20)


# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
        
# draw_spirograph(5)
screen = Screen()
screen.exitonclick()
