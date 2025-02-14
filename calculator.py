def addition(a, b):
  sum = a + b
  return sum

def subtraction(a, b):
   sub = a - b
   return sub

def multiplication(a, b):
  mul = a * b
  return mul

def division(a, b):
  if b != 0:
   div = a / b
   return div

def calculator():
  a = int(input("Enter first number: "))
  b = int(input("Enter the second number: "))
  operation = input("Enter the operation (+, -, *, /): ")

  if operation == "+":
    result = addition(a, b)
    print(f"The result of addition operation is {result}. ")
  elif operation == "-":
    result = subtractio(a, b)
    print(f"The result of the subtraction operation is {result}.")
  elif operation == "*":
    result = multiplication(a, b)
    print(f"The result of the multiplication operation is {result}.")
  elif operation == "/":
    result = division(a, b)
    print(f"The operation of the division operation is {result}.")
  else:
    print("Invalid operation.")

calculator()