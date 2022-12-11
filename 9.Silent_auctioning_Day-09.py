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