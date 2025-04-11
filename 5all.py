def all_star_patterns(n):
    def print_title(title):
        print(f"\n{'-' * 10} {title} {'-' * 10}")

    # 1. Square
    print_title("Square Pattern")
    for i in range(n):
        print('* ' * n)

    # 2. Right-Angled Triangle
    print_title("Right-Angled Triangle")
    for i in range(1, n+1):
        print('* ' * i)

    # 3. Inverted Right-Angled Triangle
    print_title("Inverted Right-Angled Triangle")
    for i in range(n, 0, -1):
        print('* ' * i)

    # 4. Pyramid
    print_title("Pyramid")
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1))

    # 5. Inverted Pyramid
    print_title("Inverted Pyramid")
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '* ' * i)

    # 6. Diamond
    print_title("Diamond")
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1))
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '* ' * (i + 1))

    # 7. Hollow Square
    print_title("Hollow Square")
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

    # 8. Hollow Pyramid
    print_title("Hollow Pyramid")
    for i in range(1, n+1):
        for j in range(n - i):
            print(' ', end='')
        for k in range(2 * i - 1):
            if k == 0 or k == 2 * i - 2 or i == n:
                print('*', end='')
            else:
                print(' ', end='')
        print()

    # 9. Right-Aligned Triangle
    print_title("Right-Aligned Triangle")
    for i in range(1, n + 1):
        print(' ' * (n - i) + '* ' * i)

    # 10. Left-Aligned Inverted Triangle
    print_title("Left-Aligned Inverted Triangle")
    for i in range(n, 0, -1):
        print('* ' * i)

    # 11. Hourglass
    print_title("Hourglass Pattern")
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '* ' * i)
    for i in range(2, n+1):
        print(' ' * (n - i) + '* ' * i)


# Call the function with any size, e.g., 5
all_star_patterns(5)
