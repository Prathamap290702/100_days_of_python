# with open ("data.csv") as file:
#     data = file.readlines()
#     print(data)
# import pandas
# import csv
# temperature = []
# with open ("data.csv") as file:
#
#     data = csv.reader(file)
#     for row in data:
#       if row[1] != "temp":
#         temperature.append(int(row[1]))
#
#     print(temperature)

# import pandas as pd
# data = pd.read_csv("data.csv")
# print(data)
# data_dict = data.to_dict()
# print(data_dict)
# temp_list =  data["temp"].to_list()
# avg_temp = sum(temp_list)/len(temp_list)
# print(avg_temp)
# print(data["temp"].max())

#get data in the column
# print(data["condition"])
# print(data.condition)

# get data in the row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp[0])
# monday_temp_F = monday_temp * 9 / 5 + 32
# print(monday_temp_F)

#Create a dataframe from scratch
# data_dict = {
    # "students": ["Amy", "James", "Pratham"],
    # "scores": [76,56,95]
# }
# data_new = pandas.DataFrame(data_dict)
# print(data)
# data_new.to_csv("new_data.csv")

# sq_data = pd.read_csv("Squirrel_Data.csv")
# My method

# f_color = sq_data.Primary_Fur_Color
# g_count = 0
# c_count = 0
# b_count = 0
# for color in f_color:
#     if color == "Gray" :
#         g_count+=1
#     elif color == "Cinnamon":
#         c_count+=1
#     elif color == "Black":
#         b_count+=1

#Easy Method
# grey_squirrels_count = len(sq_data[sq_data.Primary_Fur_Color == "Gray"])
# red_squirrels_count = len(sq_data[sq_data.Primary_Fur_Color == "Cinnamon"])
# black_squirrels_count = len(sq_data[sq_data.Primary_Fur_Color == "Black"])
#
# data_dict = {
#     "Fur Color": ["Gray", "Red", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
#
# df = pd.DataFrame(data_dict)
# print(df)
# df.to_csv("Squirrel_count.csv")

# to iterate in a dataframe you can use iterrow
# eg. for (index, row) in dataframe.iterrow():
#             print(index) --> gives index nos like 1,2,3,4 etc
#             print(row) --> this gives output as :
#               student: Angela
#               scores: 56
#               student: Tom
#               scores: 65
#               student: Jerry
#               scores: 89
# State Game
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# to get the coor of the states by clicking on the map
# def get_mouse_on_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_on_click_coor)
# turtle.mainloop()

data = pd.read_csv("50_states.csv")
data_state_list = data.state.to_list()

guessed_list = []
while len(guessed_list) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_list)}/50 States guessed", prompt="What's another state name?").title()
    if answer_state == "Exit":
        # missing_states = []
        # for state in data_state_list:
        #     if state not in guessed_list:
        #         missing_states.append(state)

        #by using data comprehension
        missing_states = [state for state in data_state_list if state not in guessed_list]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in data_state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = data[data.state == answer_state]
        t.goto(int(state.x),int(state.y))
        t.pendown()
        t.write(answer_state)
        guessed_list.append(answer_state)
