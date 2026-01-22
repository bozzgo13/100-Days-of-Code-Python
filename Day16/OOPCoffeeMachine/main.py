from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()



is_on = True
while is_on:
    options = menu.get_items()
    option = input(f"What would you like? ({options}): ")
    if option == "off":
        is_on = False
    elif option == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(option)
        print(f"Drink cost: ${drink.cost}")
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)