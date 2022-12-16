cash = 0
Menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },

}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def pay(choice):
    print("Please insert coins.")
    quarters = int(input("How many quarters? : "))
    pennies = int(input("How many pennies? : "))
    dimes = int(input("How many dimes? : "))
    nickels = int(input("How many nickels? : "))
    total = round(quarters * 0.25 + pennies * 0.01 +
                  dimes * 0.1 + nickels * 0.05, 2)
    if choice == 'espresso':
        cost = Menu['espresso']['cost']
    elif choice == 'latte':
        cost = Menu['espresso']['cost']
    elif choice == 'cappuccino':
        cost = Menu['espresso']['cost']
    # print(total)
    # print(cost)
    if cost > total:
        print("Sorry, thats not enough money.")
        return False
    elif cost <= total:
        global cash 
        cash += cost
        print(f"Enjoy your {choice}☕")
        if cost < total:
            print(f"Here's the change ${round(total-cost,2)}")
        return True


def serve(choice):
    go = pay(choice)
    if go == True:
        if choice == 'espresso':
            resources['water'] = resources['water'] - 50
            resources['coffee'] = resources['coffee'] - 18
        elif choice == 'latte':
            resources['water'] = resources['water'] - 200
            resources['milk'] = resources['milk'] - 150
            resources['coffee'] = resources['coffee'] - 24
        elif choice == 'cappuccino':
            resources['water'] = resources['water'] - 250
            resources['milk'] = resources['milk'] - 100
            resources['coffee'] = resources['coffee'] - 24


def is_enough(ingredients):
    for item in ingredients: 
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        else:
          return True


loop = True
while loop == True:
    type = input("What would you like? (Espresso/latte/cappuccino) : ").lower()
    if type == 'report':
        print(f'''Water : {resources['water']}ml
Coffee : {resources['coffee']}g
Milk : {resources['milk']}ml
Money : ${cash}''')
    elif type == 'off':
        loop = False
        print("Turning off")
    else:
        if is_enough(Menu[type]['ingredients']):
            serve(type) 
            loop = False
