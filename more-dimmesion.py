import numpy as np

# 1D array
python_list = [1, 2, 3, 4, 5]
numpy_array_from_list = np.array(python_list)
print("1D array:")
print(numpy_array_from_list)

# 2D array
two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
numpy_array_from_list_2 = np.array(two_dimensional_list)
print("\n2D array:")
print(numpy_array_from_list_2)

# 3D array
three_dimensional_list = [[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
numpy_array_from_list_3 = np.array(three_dimensional_list)
print("\n3D array:")
print(numpy_array_from_list_3)

# 4D array
four_dimensional_list = [[[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]], [[[12, 13, 14], [15, 16, 17]], [[18, 19, 20], [21, 22, 23]]]]
numpy_array_from_list_4 = np.array(four_dimensional_list)
print("\n4D array:")
print(numpy_array_from_list_4)

# 5D array
five_dimensional_list = [[[[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]], [[[12, 13, 14], [15, 16, 17]], [[18, 19, 20], [21, 22, 23]]]], [[[[24, 25, 26], [27, 28, 29]], [[30, 31, 32], [33, 34, 35]]], [[[36, 37, 38], [39, 40, 41]], [[42, 43, 44], [45, 46, 47]]]]]
numpy_array_from_list_5 = np.array(five_dimensional_list)
print("\n5D array:")
print(numpy_array_from_list_5)