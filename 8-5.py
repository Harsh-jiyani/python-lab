import array

my_array = array.array('i', [11, 22, 33, 44, 55])

# Iterating through the array
print("Iterating through the array:")
for element in my_array:
    print(element)

# Get the number of occurrences of an element
count_22 = my_array.count(22)
print("Count of 22:", count_22)

# Extend the array from another array
another_array = array.array('i', [66, 77])
my_array.extend(another_array)
print("Array after extending with another array:", my_array)

# Reverse the order of elements in the array
my_array.reverse()
print("Array after reversing:", my_array)