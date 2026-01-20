import sys # sys.exit() for exiting the application
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    }
}

resources = {
    "water": 1500,
    "milk": 600,
    "coffee": 300,
}

money = 0


def check_ingredients(water, milk, coffee):
    if water > resources["water"]:
        print(f"Sorry there is not enough water.")
        return False
    if milk > resources["milk"]:
        print(f"Sorry there is not enough milk.")
        return False
    if coffee > resources["coffee"]:
        print(f"Sorry there is not enough coffee.")
        return False

    return True

def process_coins(cost):
    global money
    print("insert coins.")

    # quarters = $0.25
    quarters = int(input("How many quarters?: "))
    # dimes = $0.10,
    dimes = int(input("How many dimes?: "))
    # nickles = $0.05,
    nickles = int(input("How many nickles?: "))
    # pennies = $0.01
    pennies = int(input("How many pennies?: "))
    total = round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01, 2)

    if total == cost:
        money += cost
        return True
    elif total < cost:
        shortage = round(cost - total, 2)
        print("Sorry that's not enough money.")
        print(f"Price: ${cost}, inserted: ${total}. shortage: ${shortage} ")
        print("Money refunded.")
        return False
    else:
        money += cost
        change = round(total - cost, 2)
        print(f"Here is ${change} dollars in change.")
        return True

def make_coffee(coffee_type, water, milk, coffee):
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee
    print(f"Here is your {coffee_type}.")

def process_order(coffee_type):
    ingredients = MENU[coffee_type]["ingredients"]
    water = 0
    milk = 0
    coffee = 0
    if "water" in ingredients:
        water = ingredients["water"]
    if "milk" in ingredients:
        milk = ingredients["milk"]
    if "coffee" in ingredients:
        coffee = ingredients["coffee"]

    cost = MENU[coffee_type]["cost"]
    if check_ingredients(water, milk, coffee):
        print(f"Your {coffee_type} costs ${cost} dollars.")
        if process_coins(cost):
            make_coffee(coffee_type, water, milk, coffee)

def order_espresso():
    process_order("espresso")

def order_latte():
    process_order("latte")

def order_cappuccino():
    process_order("cappuccino")

def turn_off_the_machine():
    print("Bye...")
    sys.exit()

def report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${money}")

procedures ={
    "espresso": order_espresso,
    "latte": order_latte,
    "cappuccino": order_cappuccino,
    "off": turn_off_the_machine,
    "report": report
}
order = input("What would you like? (espresso/latte/cappuccino):").lower()
while order in ["","espresso", "latte", "cappuccino", "off", "report"]:
    procedures[order]()
    order = input("What would you like? (espresso/latte/cappuccino):").lower()


