# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
# print(add(1,2,3,4,5,6,7,8,9,10))

# def calculate(**kwargs):
#     print(kwargs)
#     for (key,value) in kwargs.items():
#         print(key)
#         print(value)
#
# calculate(add = 5, multiply = 3)

#Lets make a class
class Car:
    def __init__(self,**kw): #kwargs optional keyword arguments
    # self.make = kw["make"] --> this type of argument passing gives error if nothing is passed so we take a give function which return none if it is empty and avoids error
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make = "NISSAN", model="GT-R")
print(my_car.make)
print(my_car.model)
# code porche 911 - gtr3rs - PRX6PHS3