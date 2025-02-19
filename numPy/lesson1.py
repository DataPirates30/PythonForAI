# import sys

# # Create a Python list with integers
# py_list = [1, 2, 3, 4, 5]
# print("Python List Memory Usage:", sys.getsizeof(py_list), "bytes")(104 bytes)
import numpy as np

arr = np.array([1,2,3,4,5],dtype = np.int32)
print(arr)
print("NumPy Array Memory Usage:", arr.nbytes, "bytes")
