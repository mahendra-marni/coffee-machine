from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
off_machine=False
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine=MoneyMachine()
while not off_machine:

    drinks = menu.get_items()
    print("what Do you like to drink ")
    drinkOfChoice = input(drinks)


    if drinkOfChoice=="off":
        off_machine=True
        break

    elif drinkOfChoice=="report":
        print(coffee_maker.resources)
        print(f"{money_machine.profit}")
    else:
        answer = menu.find_drink(drinkOfChoice)
        if (coffee_maker.is_resource_sufficient(answer))==True:
            if(money_machine.make_payment(answer.cost))==True:
                coffee_maker.make_coffee(answer)





