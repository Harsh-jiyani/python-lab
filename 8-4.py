import array

my_array = array.array('i', [100, 200, 300])
print("Original array:", my_array)

# Convert array to a list
my_list = my_array.tolist()
print("Array converted to list:", my_list)

# Convert a list to an array
new_array = array.array('i', [400, 500, 600])
another_list = [700, 800, 900]
new_array.fromlist(another_list)
print("List converted to array:", new_array)

# Get the buffer information (address and size)
buffer_info = my_array.buffer_info()
print("Buffer information (address, size):", buffer_info)

# Get the typecode of the array
print("Typecode of the array:", my_array.typecode)