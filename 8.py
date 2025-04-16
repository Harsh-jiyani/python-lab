import array

# Create an array of integers ('i' type code)
my_int_array = array.array('i', [1, 2, 3, 4, 5])
print("Integer array:", my_int_array)

# Create an array of doubles ('d' type code)
my_double_array = array.array('d', [1.0, 2.5, 3.7, 4.2, 5.9])
print("Double array:", my_double_array)

# Create an empty array and then extend it
empty_array = array.array('i')
empty_array.extend([10, 20, 30])
print("Extended empty array:", empty_array)
