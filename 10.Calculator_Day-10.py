# functions with output
# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"{formatted_f_name} {formatted_l_name}"


# name = format_name("pratham", "prajapatI")
# print(name)

#Days in months
# def leap_year(year):
#     # is_leap_year = False
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 is_leap_year = True
#             else:
#                 is_leap_year = False
#         else:
#             is_leap_year = True
#     else:
#         is_leap_year = False

#     if year % 400 == 0:
#         print("Leap Year.")
#     return is_leap_year


# def days_of_months(year, month):
#     leap = leap_year(year)
#     if leap == False:
#         days = day[month - 1]
#     elif leap == True and month == 2:
#         days = day[month-1] + 1
#     return days


# day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# year = int(input("Enter the year : "))
# month = int(input("Enter the month : "))
# days = days_of_months(year, month)
# print(f"The {month} of {year} has {days} days in it.")
