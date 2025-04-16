import array

my_array = array.array('i', [10, 20, 30, 40, 50])

# Accessing elements by index
print("Element at index 0:", my_array[0])
print("Element at index 3:", my_array[3])
print("Last element:", my_array[-1])

# Slicing the array
print("Slice from index 1 to 3:", my_array[1:4])

# Modifying an element
my_array[2] = 35
print("Array after modification:", my_array)