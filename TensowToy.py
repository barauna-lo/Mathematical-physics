import numpy as np
import tensorflow

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
newarr = np.reshape(arr, (3,4,1))
newarr2 = tensorflow.reshape(arr, (3,4,1))

type(newarr2)
