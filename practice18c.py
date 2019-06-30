import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# arr3 = np.array([[[],[]]])

print(arr1)
print(arr2)

print(len(arr1))
print(len(arr2))

print(arr1[1])
print(arr2[1][2])

print("arr1 shape is: ", arr1.shape)
print("arr2 shape is: ", arr2.shape)
print("arr2 shape[0] is: ", arr2.shape[0])

a1 = np.ones(8)
print(a1)

a4 = np.zeros(8)
print(a4)

print()

print(a1.shape)

a2 = a1.reshape(2, 2, 2)
print(a1)
print(a2)

a3 = a2.ravel()                 # for getting back to the original shape
print(a3)