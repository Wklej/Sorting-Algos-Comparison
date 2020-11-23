import random
from enum import Enum
from QsortHoare import quickSort
from RadixSort import radix, __get_num_digits
from HeapSort import heapSort
import numpy as np
import time


class Algos(Enum):
    heapSort, quickSort, radixSort = range(3)


def createArray(elements, rangefrom, rangeto):
    return np.array([random.randint(rangefrom, rangeto) for _ in range(elements)])


# Dictionary with times of sorting algorithms
times = {'quickSort': [],
         'heapSort': [],
         'radixSort': []}


def sort(algorithm, sizeOfArray, arr_):
    if algorithm == Algos.heapSort:
        heapSort(arr_)
    elif algorithm == Algos.radixSort:
        radix(arr_, __get_num_digits(arr_))
    elif algorithm == Algos.quickSort:
        quickSort(arr_, 0, sizeOfArray - 1)


def rad(algo, array):
    if algo == Algos.radixSort:
        return radix(array, __get_num_digits(array))


samples = [100000, 1000000]


for i in range(len(samples)):
    arr = createArray(samples[i], 0, 1000)
    print("{} :".format(samples[i]))
    for algo in Algos:
        arr_copy = arr.copy()
        t0 = time.time()
        if algo != Algos.radixSort:
            sort(algo, samples[i], arr_copy)
        else:
            arr_copy = radix(arr_copy, __get_num_digits(arr_copy))
       # print("sorted by: {}  : {}".format(algo.name, arr_copy[3:-3]))
        t1 = time.time()
        tot_time = t1 - t0
        times[str(algo.name)].append(tot_time)
        print("{}: {}".format(str(algo.name), times[str(algo.name)][i]))
