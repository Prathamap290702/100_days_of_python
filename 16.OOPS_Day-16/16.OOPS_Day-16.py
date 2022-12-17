# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green","red")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("POkeMon Name", ["Pikachu", "charizard", "Squirtle"])
# table.add_column("Type", ["Electric", "Fire", "Water"])
# table.align = "l"
# print(table)

# Coffee machine using OOPS
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

money_machine.report()
coffee_maker.report()


while is_on:
    option = menu.get_items()
    choice = input(f"What would you like ? ({option}) : ").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(choice) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
