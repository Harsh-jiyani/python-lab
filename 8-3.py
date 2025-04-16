import array

my_array = array.array('i', [1, 2, 3, 4, 5])
print("Original array:", my_array)

# Append an element to the end
my_array.append(6)
print("Array after appending 6:", my_array)

# Insert an element at a specific index
my_array.insert(2, 15)
print("Array after inserting 15 at index 2:", my_array)

# Remove the first occurrence of a value
my_array.remove(3)
print("Array after removing the first 3:", my_array)

# Pop the last element
last_element = my_array.pop()
print("Array after popping:", my_array)
print("Popped element:", last_element)