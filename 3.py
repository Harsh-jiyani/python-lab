def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

fifth_fibonacci = fibonacci(5)
print("The 5th Fibonacci number is:", fifth_fibonacci)
