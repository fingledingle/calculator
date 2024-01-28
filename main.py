def add(n1, n2):
    return n1 + n2


#Subtract
def subtract(n1, n2):
    return n1 - n2


#Multiply
def multiply(n1, n2):
    return n1 * n2


#Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator ():
  from art import logo
  print(logo)
  num1 = float(input("What is the first number? \n"))
  
  for symbol in operations:
      print(symbol)
  
  
  continuation_or_not = True
  
  while continuation_or_not:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the second number? \n"))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
  
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: "):
      num1 = answer
    else:
      continuation_or_not = False
      calculator ()
      
calculator ()