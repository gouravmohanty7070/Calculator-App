#Calculator

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

num1 = int(input("What's the first number? "))
num2 = int(input("What's the second number? "))

for i in application:
  print(i)
operation_symbol = input("Pick an symbol from the line above: ")

function = application[operation_symbol]
answer = function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
