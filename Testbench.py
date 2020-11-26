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


def createArrayDesc(elements):
    arr_desc = np.array([0 for _ in range(elements)])
    for i in range(elements):
        arr_desc[i] = elements - i
    return arr_desc


def sort(algorithm, sizeOfArray, arr_):
    if algorithm == Algos.heapSort:
        heapSort(arr_)
    elif algorithm == Algos.radixSort:
        radix(arr_, __get_num_digits(arr_))
    elif algorithm == Algos.quickSort:
        quickSort(arr_, 0, sizeOfArray - 1)


# Dictionary with times of elements
# times = {'quickSort': {
#             'range': [],
#             'elements': []},
#          'heapSort': {
#               'range': [],
#               'elements': []},
#          'radixSort': {
#              'range': [],
#              'elements': []}}


ranges = [100, 1000, 10000, 100000, 1000000]
samples = [50000, 100000, 500000, 1000000, 50000000]

times = {
    Algos.quickSort.name: {
        ranges[0]: [],
        ranges[1]: [],
        ranges[2]: [],
        ranges[3]: [],
        ranges[4]: []
    },
    Algos.heapSort.name: {
            ranges[0]: [],
            ranges[1]: [],
            ranges[2]: [],
            ranges[3]: [],
            ranges[4]: []
     },
    Algos.radixSort.name: {
            ranges[0]: [],
            ranges[1]: [],
            ranges[2]: [],
            ranges[3]: [],
            ranges[4]: []
        }
}


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

# for i in range(len(samples)):
#     arr = createArrayDesc(samples[i])
#     print("{} :".format(samples[i]))
#     for algo in Algos:
#         arr_copy = arr.copy()
#         t0 = time.time()
#         if algo != Algos.radixSort:
#             sort(algo, samples[i], arr_copy)
#         else:
#             arr_copy = radix(arr_copy, __get_num_digits(arr_copy))
#        # print("sorted by: {}  : {}".format(algo.name, arr_copy[3:-3]))
#         t1 = time.time()
#         tot_time = t1 - t0
#         times[str(algo.name)].append(tot_time)
#         print("DESC {}: {}".format(str(algo.name), times[str(algo.name)][i]))


# array = createArray(1000, 0, 1000)
# array2 = np.array([0 for _ in range(100000)])
# print(array2)
# quickSort(array2, 0, 100000 - 1)
# print(array2)
