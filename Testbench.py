import random
from QsortHoare import quickSort
from RadixSort import radix, __get_num_digits
from HeapSort import heapSort
import numpy as np
import time


def createArray(elements, rangefrom, rangeto):
    return np.array([random.randint(rangefrom, rangeto) for _ in range(elements)])


# Array to test
sizeOfArray = 100000
arr = createArray(sizeOfArray, 0, 1000)

# Dictionary with times of sorting algorithms
times = {'quickSort': [],
         'heapSort': [],
         'radixSort': []}

for i in range(3):
    if i == 0:
        t0 = time.time()
        quickSort(arr, 0, sizeOfArray - 1)
        t1 = time.time()
        tot_time = t1 - t0
        times['quickSort'].append(tot_time)
        print("quicksort: {}".format(times['quickSort']))
    if i == 1:
        t0 = time.time()
        radix(arr, __get_num_digits(arr))
        t1 = time.time()
        tot_time = t1 - t0
        times['radixSort'].append(tot_time)
        print("radixSort: {}".format(times['radixSort']))
    if i == 2:
        t0 = time.time()
        heapSort(arr)
        t1 = time.time()
        tot_time = t1 - t0
        times['heapSort'].append(tot_time)
        print("heapSort: {}".format(times['heapSort']))

# for key, value in times.items():
#     print("{} : {}".format(key, value))