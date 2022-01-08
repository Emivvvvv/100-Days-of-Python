import data


def check(coffee_type):
    coffee_type_water = data.MENU[coffee_type]["ingredients"]["water"]
    coffee_type_milk = data.MENU[coffee_type]["ingredients"]["milk"]
    coffee_type_coffee = data.MENU[coffee_type]["ingredients"]["coffee"]
    resource_water = data.resources["water"]
    resource_milk = data.resources["milk"]
    resource_coffee = data.resources["coffee"]
    not_enough = ""
    if resource_coffee < coffee_type_coffee:
        not_enough += " coffee"
    if resource_milk < coffee_type_milk:
        not_enough += " milk"
    if resource_water < coffee_type_water:
        not_enough += " water"
    if not_enough != "":
        print(f"Sorry, there is not enough{not_enough}")
        return False
    else:
        return True


def make_coffee(coffee_type):
    data.resources["water"] -= data.MENU[coffee_type]["ingredients"]["water"]
    data.resources["milk"] -= data.MENU[coffee_type]["ingredients"]["milk"]
    data.resources["coffee"] -= data.MENU[coffee_type]["ingredients"]["coffee"]


def get_coins_and_serve_the_coffee(coffee_type):
    print("Please insert coins.")
    quarter = int(input("How many quarter"))
    dimes = int(input("How many dimes"))
    nickel = int(input("How many nickel"))
    pennies = int(input("How many pennies"))
    total = quarter*0.25 + dimes*0.1 + nickel*0.05 + pennies*0.01
    if total > data.MENU[coffee_type]["cost"]:
        print(f'Here is ${total- data.MENU[coffee_type]["cost"]} in change.')
        data.resources["money"] = data.MENU[coffee_type]["cost"]
        make_coffee(coffee_type)
        print(f"Here is your {coffee_type} {data.coffee_emoji} enjoy!")
        return 0
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 1


def refill_and_cashout():
    data.resources["water"] += int(input("Water: "))
    data.resources["milk"] += int(input("Milk: "))
    data.resources["coffee"] += int(input("Coffee: "))
    cashout = input("Do you want to cash out? ")
    if cashout == "y":
        print(f'${data.resources["money"]} cashed out.')
        data.resources["money"] = 0
    else:
        print("Closing refill and cash out mode!!!\n###################################")


def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice != "espresso" and choice != "latte" and choice != "cappuccino" and choice != "off" and choice != "report" and choice != "refill&cashout":
            print("You typed wrong.")
        elif choice == "off":
            exit()
        elif choice == "refill&cashout":
            refill_and_cashout()
        elif choice == "report":
            print("The current resource values")
            print(f'Water: {data.resources["water"]}\nMilk: {data.resources["milk"]}\nCoffee: {data.resources["coffee"]}\nMoney: {data.resources["money"]}')
        elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
            if check(choice):
                get_coins_and_serve_the_coffee(choice)
            else:
                print("Please try to get other coffee or wait for resources to be refilled.")
        else:
            print("Something went wrong! Please inform that report at www.amoguscoffemachinesinfnaf.com")


coffee_machine()
