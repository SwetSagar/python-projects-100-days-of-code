import os
import art
print(art.logo)

def add(n1, n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  
  n1 = float(input("What's the first number?: "))
  
  for symbol in operations:
    print(symbol)
    
  user_input  = input("What operation do you want to perform? ")
  
  calculator_running = True
  
  while calculator_running :
    n2 = float(input("What's the next number?: "))
    calculation_function = operations[user_input]
    answer = calculation_function(n1,n2)
    print(f"{n1} {user_input} {n2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      n1 = answer
    else:
      calculator_running = False
      os.system('cls')
      calculator()

calculator()
        