from calc_art import logo

print(logo)

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

math_op = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide
}
def calculator():
  num1 = int(input("First number: "))
  for key in math_op:
    print(key)
  should_continue = True

  while should_continue == True:
    user_choice = input("Pick an operation: ")
    num2 = int(input("Second number: "))
    for key in math_op:
      if key == user_choice:
        answer = int(math_op[key](num1, num2))

    print(f"{num1} {user_choice} {num2} = {answer}")

    if input("Type y to continue or n to start new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()
