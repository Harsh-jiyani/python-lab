# Demonstrate dictionary operations in Python

# Create a dictionary
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Add a new key-value pair
person['job'] = 'Engineer'

# Update an existing key
person['age'] = 31

# Delete a key-value pair
del person['city']

# Iterate over dictionary items
for key, value in person.items():
    print(f"{key}: {value}")
