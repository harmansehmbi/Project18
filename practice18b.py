import numpy as np

numbers = (10, 20, 30, 40, 50)
print(numbers, type(numbers))

print()

# Pass List/Tuple/Set/Dictionary/String i.e. all the sequences

array = np.array([10, 20, 30 ,40 ,50])
print(array, type(array))

# Check Size

print(len(array))

print()

# Update Data in Array

array[2] = 222

array2 = np.append(array, [11, 12, 13])
print(array2)

print()

# For Iteration in array

for elm in array:
    print(elm)