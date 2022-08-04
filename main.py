#Calculator
from art import logo


#ADD
def add(n1, n2):
  return n1 + n2

#SUBSTRACT
def sub(n1, n2):
  return n1 - n2

#MULTIPLY
def mul(n1, n2):
  return n1 * n2

#Divide
def div(n1, n2):
  return n1 / n2

#Dictionary
application = {
  '+': add,
  '-': sub,
  '*': mul,
  '/': div
}
def calculator():
  print(logo)
  num1 = float(input("What's the first number? "))
  
  for i in application:
    print(i)
  operation_symbol = input("Pick an symbol from the line above: ")
  
  flag = True
  
  answer = num1 
  
  while flag:
    num2 = float(input("What's the next number? "))
    
    function = application[operation_symbol]
    answer = function(num1,num2)
  
  
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    repeat = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
  
    if repeat == "y":
      operation_symbol = input("Pick an operation: ")
      num1 = answer
    else:
      flag = False
      calculator()

calculator()