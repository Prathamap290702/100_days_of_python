# #inheritance

# class animal:
#     def  __init__(self):
#       self.num_eyes = 2

#     def breathe(self):
#         print("Inhale, Exhale.")

# class fish(animal):
#     def __init__(self):
#       super().__init__()
#     def swim(self):
#         print("Moving underwater.")
#     def breathe(self):
#         super().breathe()
#         print("Doing this underwater.")


# nemo = fish()
# nemo.breathe()

from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
