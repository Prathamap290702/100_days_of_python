from turtle import Turtle, Screen

# import turtle
# tim = turtle.Turtle()//every time we have to write turtle.

# from turtle import * //import everything

#import turtle as t //alias

tim = Turtle()
tim.shape("turtle")
tim.color("red")
# tim.forward(100)

#make square
# for i in range(0,4):
#     tim.forward(100)
#     tim.left(90)

#dashed lines
for _ in range(0,15):
    tim.forward(10)
    tim.pu()
    tim.forward(10)
    tim.pd()












screen = Screen()
screen.exitonclick()