
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
    print(f"{num1} + {num2} = {addition()}")
elif sign == '-':
    print(f"{num1} - {num2} = {subtraction()}")
elif sign == '*': 
    print(f"{num1} * {num2} = {multiplication()}")
elif sign == '/':
    print(f"{num1} / {num2} = {division()}")
else:
    print("Invalid operation. Please enter one of +, -, *, /.")
# End of calculator/calc.py

