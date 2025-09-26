# calculator/calc_fixed.py

# Input is fine as is
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sign = input("Enter operation (+, -, *, /): ")

# Functions now take num1 and num2 as arguments
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        # Returning None or raising an exception is better, but for consistency,
        # we'll return a special error string for now.
        return "Error: Division by zero is not allowed."
    return a / b

# Main logic needs to pass the numbers and handle the division error gracefully
if sign == '+':
    result = addition(num1, num2)
    print(f"{num1} + {num2} = {result}")

elif sign == '-':
    result = subtraction(num1, num2)
    print(f"{num1} - {num2} = {result}")

elif sign == '*':
    result = multiplication(num1, num2)
    print(f"{num1} * {num2} = {result}")

elif sign == '/':
    result = division(num1, num2)
    # Check if the result is the error string before printing the calculation
    if isinstance(result, str) and "Error" in result:
        print(result) # Print the error message directly
    else:
        print(f"{num1} / {num2} = {result}")

else:
    print("Invalid operation. Please enter one of +, -, *, /.")
# End of calculator/calc_fixed.py
