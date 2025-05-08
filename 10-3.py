# Demonstrate file handling in Python

filename = "example.txt"

# Write to a file
with open(filename, 'w') as file:
    file.write("Hello, world!\n")
    file.write("This is a test file.\n")

# Read from the file
with open(filename, 'r') as file:
    content = file.read()
    print("File content after writing:")
    print(content)

# Append to the file
with open(filename, 'a') as file:
    file.write("Appending a new line.\n")

# Read again to show appended content
with open(filename, 'r') as file:
    content = file.read()
    print("File content after appending:")
    print(content)
