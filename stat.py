import numpy as np
# Creating python List
python_list = [1,2,3,4,5]

# Checking data types
print('Type:', type (python_list)) # <class 'list'>
#
print(python_list) # [1, 2, 3, 4, 5]

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]

print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# Creating Numpy(Numerical Python) array from python list

numpy_array_from_list = np.array(python_list, dtype=float)
print(type (numpy_array_from_list))   # <class 'numpy.ndarray'>
numpy_array_from_list_2 = np.array(two_dimensional_list)
print(numpy_array_from_list) # array([1, 2, 3, 4, 5])
print(numpy_array_from_list_2)