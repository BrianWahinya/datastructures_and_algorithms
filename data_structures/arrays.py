# Arrays
# In Python: Arrays are referred to as Lists
from utils import clear_cmd, generate_unordered_integers

clear_cmd()
print('''
####### Arrays (or Lists in Python) ######
''')

# Heterogeneous
array = [2552, 73676, 9899, "example"]
sub_array_one = generate_unordered_integers(55, 70)
sub_array_two = generate_unordered_integers(121, 140)
strings = ["Orange", "mango", "Kiwi", "pineapple", "banana"]

# add element in the end
array.append(23)
print("Append", array)

# insert element at specific position
array.insert(2, 78)
print("Insert", array)

# remove element
array.remove("example")
print("Remove", array)

# change element
array[1] = 335
print("Change", array)

# reverse array
array.reverse()
print("Reverse", array)

# sort element
# default: asc
array.sort()
print("Sort: asc", array)

array.sort(reverse=True)
print("Sort: desc", array)

# case-sensitive: capital letters are sorted first
strings.sort()
print("Sort: case-sensitive", strings)

# case-insensitive
strings.sort(key=str.lower)
print("Sort: case-insensitive", strings)

# clear all elements in array
array.clear()
print("Clear", array, '\n')

# Extend two arrays
print("array=", array)
print("sub_array_one=", sub_array_one)
print("sub_array_two=", sub_array_two)
array.extend(sub_array_one)
print("Extend array:subarr_one", array, '\n')

sliced_arr = array[:3]
sliced_sub = sub_array_two[:5]
sliced_arr.extend(sliced_sub)
print("Slice & extend", sliced_arr)

# Copy
merged = sliced_arr.copy()
merged[0] = 0
print("Copy vs extend")
print("merged=", merged)
print("extended=", sliced_arr)