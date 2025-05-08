# Demonstrate function definitions and usage in Python

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def factorial(n):
    """Return the factorial of a non-negative integer n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Using the functions
print(greet("Alice"))
print("Sum of 5 and 3 is:", add(5, 3))
print("Factorial of 5 is:", factorial(5))
