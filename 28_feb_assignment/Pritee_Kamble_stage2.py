# Basic calculator
num1 = float(input("Enter first Number: "))
num2 = float(input("Enter second Number: "))
operator = input("Enter operator (+,-,*,/)")
if operator == "+":
  result = num1 + num2
  print("Result = ",result)
elif operator == "-":
  result = num1 - num2
  print("Result = ",result)
elif operator == "*":
  result = num1 * num2
  print("Result = ",result)
elif operator == "/":
  if num2 == 0:
    print("Error: Divison by zero is not allowed")
  else:
    result = num1 / num2
    print("Result = ",result)
else:
  print("Invalid operator ",operator)

# checking result is positive, negative, or zero
if result > 0:
  print("Positive")
elif result < 0:
  print("Negative")
else:
  print("zero")