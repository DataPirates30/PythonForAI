# Why to use numpy when you have python list?
import sys
import numpy as np

# So the first difference is that numpy store data in contiguous blocks of memory
# and python list store data in non-contiguous blocks of memory
# So if we check the size of python list and numpy array
# we will see that numpy array is smaller than python list

my_list = []
my_array = np.array(my_list)

# An empty list takes 56 bytes of base memory in python 
print(sys.getsizeof(my_list)) # 56
my_list = [1,2,3]
print(sys.getsizeof(my_list)) # 88(Extra memory for frequent resizing)




