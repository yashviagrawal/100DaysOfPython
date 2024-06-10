from Days.Day17.menu import Menu
from Days.Day17.coffee_maker import CoffeeMaker
from Days.Day17.money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
cashier = MoneyMachine()
while True:
    choice = input(f"Enter choice {menu.get_items()}: ").lower()
    if choice == "report":
        coffee_maker.report()
        cashier.report()
    elif choice == "off":
        isOn = False
        print("Turning Machine Off")
        break;
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if cashier.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
