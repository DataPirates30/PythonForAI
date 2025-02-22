# import sys

# # Create a Python list with integers
# py_list = [1, 2, 3, 4, 5]
# print("Python List Memory Usage:", sys.getsizeof(py_list), "bytes")(104 bytes)
import numpy as np
import ctypes


def creating1DAray():
    # int32 allocates 4 bytes for int, 64 allocates 8 bytes for int
    myArr = np.array([[10,20,0],[30,40,50]], dtype = np.int32) 
    print(myArr.itemsize)
    print(myArr.shape)


    

def main():
    def pointerBehavior():
        arr = np.array([1,2,3,4,5],dtype = np.int32)
        ptr = arr.ctypes.data
        for i in range(arr.size):
            print(f"Element:{i}, Address:{ptr+i*arr.itemsize}, Value = {arr[i]}")

    def creating2DArray():
        my2D = np.array([[1,2,3],[4,5,6]])
        print(my2D)

    # pointerBehavior()


if __name__ == "__main__":
    # main()
    creating1DAray()


