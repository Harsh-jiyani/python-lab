password = input("Enter a password: ")

if len(password) < 6:
    print("Weak password (too short)")
elif password.isdigit() or password.isalpha():
    print("Weak password (add mix of letters and numbers)")
else:
    print("Strong password 💪")
