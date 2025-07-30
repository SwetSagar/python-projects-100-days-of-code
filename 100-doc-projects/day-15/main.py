import art
print('Welcome to my Coffee Machine Project!')
print(art.logo)



resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,}

profit = 0.0


menu = {    "espresso": {
        "ingredients": {
            "Water": 50,
            "Coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "Water": 200,
            "Milk": 150,
            "Coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "Water": 250,
            "Milk": 100,
            "Coffee": 24,
        },
        "cost": 3.0,
    }
}


def is_resource_sufficient(order_ingredients):
    """Returns True if resources are sufficient, False if not."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def is_transaction_succesful(money_received, drink_cost):
    """Returns True if the transaction is successful, False if not."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

# Variable to keep track of the coffee machine state
coffee_machine_running = True
# This loop simulates the coffee machine operation
while coffee_machine_running:
    # Simulating a coffee machine operation
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    # Print report
    if user_input == "report":
        print(f"Water: {resources['Water']}ml")
        print(f"Milk: {resources['Milk']}ml")
        print(f"Coffee: {resources['Coffee']}g")
        print(f"Money: ${resources['Money']:.2f}")
        continue  # Skip the rest of the loop and prompt againre
    elif user_input == "off":
        coffee_machine_running = False
        print("Turning off the coffee machine. Goodbye!")
    else :
        drink = menu.get(user_input)
        if is_resource_sufficient(drink["ingredients"]) :
            payment = process_coins()
            if is_transaction_succesful(payment, drink["cost"]):
                make_coffee(user_input, drink["ingredients"])
