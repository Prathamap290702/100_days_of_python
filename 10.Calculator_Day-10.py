# functions with output
# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"{formatted_f_name} {formatted_l_name}"


# name = format_name("pratham", "prajapatI")
# print(name)

# Days in months
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
#     """Takes month and year and returns the number of days in that particaular month."""#Docstring used for writing the documentation for any function
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

# Calculator
import os
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(num1, num2):
    return num1 + num2


def multiply(num1, num2):
    return num1 * num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2


operations_list = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def Calculate():
    print(logo)
    num1 = float(input("Enter the first number : "))
    on = True
    while on == True:
        operations = input(('''Operations : +
                    -
                    *
                    /\n : '''))
        num2 = float(input("Enter the next number : "))
        operate = operations_list[operations]
        answer = operate(num1, num2)
        print(f"{num1} {operations} {num2} = {answer}")
        loop = int(input(f'''1. Do you want to continue with {answer}
        2.You want to start new operation
        3.You want to stop ? : '''))
        if loop == 1:
            num1 = answer
        elif loop == 2:
            os.system('cls')
            Calculate()
        elif loop == 3:
            print("Thank you for using the calculator....")
            on == False
            return


Calculate()
