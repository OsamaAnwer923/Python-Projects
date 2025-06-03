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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0
def is_resource_sufficient(order_ingredient):
    for items in order_ingredient:
        if order_ingredient[items] >= resources[items]:
            print(f"there is no enough resources {items}")
            return False
        return True
machine=True
while machine==True:
    order = input('What would you like? (espresso/latte/cappuccino):').lower()
    if order == 'off':
        machine=False
    elif order=='report':
        print(f" water: {resources['water']}ml")
        print(f" milf: {resources['milk']}ml")
        print(f" coffee: {resources['coffee']}g")
        print(f" profit: ${profit}")
    else:
        print(f"your order is {order} of price ${MENU[order]['cost']}")
        if is_resource_sufficient(MENU[order]['ingredients']):
            for items in MENU[order]['ingredients']:
                resources[items] -= MENU[order]['ingredients'][items]
            profit += MENU[order]['cost']
            print("Thanks for your order")
         
        
         