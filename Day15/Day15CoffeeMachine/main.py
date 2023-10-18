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
  "water": 500,
  "milk": 500,
  "coffee": 500,
}


def check_resources(drink):
  make_drink = True
  for item in MENU:
    if item == drink:
      ingredients = MENU[item]["ingredients"]
  for ing in resources:
    if ing in ingredients:
      if resources[ing] < ingredients[ing]:
        print(f"Insufficient ingredients. Not enough {ing}")
        make_drink = False
        money = False
  if make_drink:
    boolean, money = check_money(drink)
    if boolean:
      for ing in ingredients:
        resources[ing] -= ingredients[ing]
        print(f'There is {resources[ing]} {ing} left')
    else:
      print(f"You do not have enough money to purchase {drink}")
      make_drink = False
      return make_drink, money
  return make_drink, money


def check_money(order):
  dollar = float(input("Enter the amount of dollar bills: "))
  quarter = float(input("Enter the amount of quarters: "))
  dime = float(input("Enter the amount of dimes: "))
  nickel = float(input("Enter the amount of nickels: "))
  penny = float(input("Enter the amount of penny: "))
  quarter *= .25
  dime *= .1
  nickel *= .05
  penny *= .01
  total = round(dollar + quarter + dime + nickel + penny, 2)
  price = round(MENU[order]["cost"], 2)
  if total >= price:
    change = total - price
    return True, change
  else:
    return False, False


def check_input(user):
  if user == 'e' or user == 'espresso':
    drink = 'espresso'
  elif user == 'l' or user == 'latte':
    drink = 'latte'
  elif user == 'c' or user == 'cappuccino':
    drink = 'cappuccino'
  else:
    print("Please use the correct character to select your drink.")
    operate()
    return
  make_drink, money = check_resources(drink)
  if make_drink:
    if money >= 0:
      return drink, money
  else:
    return make_drink, money


def operate():
  profit = 0
  user = input("What would you like? \nE - espresso $1.50 \nL - latte $2.50 \nC - cappuccino $3.00 \n").lower()
  if user == "off":
    print("Turning the machine off.")
    return
  elif user == "report":
    print(resources)
    print(f"The coffee machine has made ${profit} so far")
    operate()
    return
  else:
    result_drink, result_change = check_input(user)
    # print(result_drink, result_change)
    if result_drink is False:
      operate()
      return
    else:
      print(f"Here is your {result_drink}, with change of ${result_change}")
      profit += MENU[result_drink]["cost"]
      operate()
      return


operate()
