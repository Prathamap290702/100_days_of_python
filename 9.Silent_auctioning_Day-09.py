# #Dictionary
# programming_dictionary = {
#     "Bug" :  "An error",
#     "Function" : "that can be called again and again.",
# }
# #retrieving value
# print(programming_dictionary["Bug"])

# #adding new entry
# programming_dictionary["loop"] ="the action of doing something again and again."
# # print(programming_dictionary)

# # empty_dict = {}
# # programming_dictionary = {}
# # print(programming_dictionary)#wiping dictionary

# #edit dictionary
# # programming_dictionary["Bug"] = "new value"
# # print(programming_dictionary["Bug"])

# #looping in dictionary
# for keys in programming_dictionary:
#     print(keys)
#     print(programming_dictionary[keys])

# grading program
# students_scores = {"S1": 99,
#                    "S2": 100,
#                    "S3": 75,
#                    "S4": 54,
#                    "S4": 84,
#                    "S5" : 33}
# students_grades = {}
# for names in students_scores:
#     if students_scores[names] > 90 and students_scores[names] <= 100:
#         students_grades[names] = "A"
#     elif students_scores[names] > 80 and students_scores[names] <= 90:
#         students_grades[names] = "B"
#     elif students_scores[names] > 70 and students_scores[names] <= 80:
#         students_grades[names] = "C"
#     elif students_scores[names] > 60 and students_scores[names] <= 70:
#         students_grades[names] = "D"
#     elif students_scores[names] > 50 and students_scores[names] <= 60:
#         students_grades[names] = "E"
#     else:
#         students_grades[names] = "FAIL"
# print(students_grades)

# # nesting
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin"
# }
# #list in dictionary
# travel_log = {
#     "France": ["Paris", "lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }
# #dictionary in dictionary
# travel_log = {
#     "France": {"Cities_vistied": ["Paris", "lille", "Dijon"], "Total_visits": 12},
#     "Germany": {"Cities_vistied": ["Berlin", "Hamburg", "Stuttgart"], "Total_visits": 12}
#     }
# #dictionary in list
# travel_log = [
#     {"Country" : "France" ,"Cities_vistied" : ["Paris", "lille", "Dijon"], "Total_visits": 12},
#     {"Country" :"Germany", "Cities_vistied": ["Berlin", "Hamburg", "Stuttgart"], "Total_visits": 5}
# ]

# travel_log = [
#     {"Country" : "France" ,"Cities_vistied" : ["Paris", "lille", "Dijon"], "Total_visits": 12},
#     {"Country" :"Germany", "Cities_vistied": ["Berlin", "Hamburg", "Stuttgart"], "Total_visits": 5}
# ]
# def add_new_country(country_visited, times_visited, cities_visited):
#     new_country = {}
#     new_country["Country"] = country_visited
#     new_country["Total_visits"] = times_visited
#     new_country["Cities_visited"] = cities_visited
#     travel_log.append(new_country)

# add_new_country("Russia", 2, ["Moscow", "St. Petersburg"])
# print(travel_log)


# Silent auction
import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)


def add_new_bidder(key, value):
    bids[key] = value

def winner():
    max = 0
    win = ""
    for keys in bids:
        if bids[keys] >= max:
            max = bids[keys]
            win = keys
    print(f"The winner of bid is {win} with a bid of ${max}.")
auction = True
bids = {}
while auction:
    key = input("What is your name : ")
    value = int(input("What is your Bid price : $"))
    add_new_bidder(key, value)
    loop = input("Are there any more bidders (Y/N) : ").lower()
    if loop == "y":
        os.system('cls')
    else:
        auction = False
        winner()

