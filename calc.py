
#calculator/calc.py

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sign = input("Enter operation (+, -, *, /): ")

def subtraction():
    return num1 - num2
def multiplication():
    return num1 * num2
def division():
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2  

def addition():
    return num1 + num2

if sign == '+':
    addition_result = addition()
    print(f"{num1} + {num2} = {addition_result}")
elif sign == '-':
    subtraction_result = subtraction()
    print (f"{num1} - {num2} = {subtraction_result}")
  
elif sign == '*': 
    multiplication_result = multiplication()
    print(f"{num1} * {num2} = {multiplication_result}")

elif sign == '/':
    division_result = division()
    print(f"{num1} / {num2} = {division_result}")
else:
    print("Invalid operation. Please enter one of +, -, *, /.")
# End of calculator/calc.py

