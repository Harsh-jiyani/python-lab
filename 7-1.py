def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

# Main logic
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == '1':
    print(f"Result: {add(num1, num2)}")
elif operation == '2':
    print(f"Result: {subtract(num1, num2)}")
elif operation == '3':
    print(f"Result: {multiply(num1, num2)}")
elif operation == '4':
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid input!")
