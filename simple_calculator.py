def add(x, y):#adding to numbers together
    return x + y

def subtract(x, y):#subtracting second number from first
    return x - y

def multiply(x, y):#multiplying two numbers
    return x * y

def divide(x, y):#dividing first number by second
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def exponent(x, y):#multiplying the first number by itself y times
    return x ** y

def modulus(x, y):#division, but only returns the remainder
    if y == 0:
        return "Error: Modulus by zero is not allowed."
    return x % y

def floor_division(x, y):#division, but rounds down to the nearest whole number
    if y == 0:
        return "Error: Floor division by zero is not allowed."
    return x // y

operation = input("Welcome to this extremely basic calculator! Please enter the number that corresponds to the function you would like to use: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Modulus\n7. Floor Division\n")

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

if operation not in ['1', '2', '3', '4', '5', '6', '7']:
    print("Invalid input. Please enter a number between 1 and 7.")
    exit()
if operation == '1':
    result = add(x, y)
elif operation == '2':
    result = subtract(x, y)
elif operation == '3':
    result = multiply(x, y)
elif operation == '4':
    result = divide(x, y)
elif operation == '5':
    result = exponent(x, y)
elif operation == '6':
    result = modulus(x, y)
elif operation == '7':
    result = floor_division(x, y)

print("The result is:", result)