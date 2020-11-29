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

def save_file(name, times_):
    with open("{}.csv".format(name), 'w') as f:
        for i in times_: #3 times
            f.write("\n{}".format(i))
            for j in times_[i].values(): # 5 times
                f.write("\n")
                for x in j:
                    f.write("{};".format(x))


ranges = [100, 1000, 10000, 100000, 1000000]
samples = [50000, 100000, 500000, 1000000, 50000000]
#samples = [10000, 100000]

for i in range(5):

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

    timesHR = {
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

    times4R = {
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

    # SORTING RANDOM ARRAY
    for range_ in range(len(ranges)):
        for sample_ in range(len(samples)):
            arr = createArray(samples[sample_], 0, ranges[range_])
            for algo in Algos:
                print(algo.name)
                arr_copy = arr.copy()
                t0 = time.time()
                if algo != Algos.radixSort:
                    sort(algo, samples[sample_], arr_copy)
                else:
                    arr_copy = radix(arr_copy, __get_num_digits(arr_copy))
                t1 = time.time()
                tot_time = t1 - t0
                times[algo.name][ranges[range_]].append(tot_time)
                print("range: {} sample: {} - {}".format(ranges[range_], samples[sample_], tot_time))

    save_file("outRANDOMTEST{}".format(i), times)

    #  SORTING HALF RANDOM ARRAY
    for range_ in range(len(ranges)):
        for sample_ in range(len(samples)):
            arr1 = createArray(samples[sample_] - 7000, 0, ranges[range_])
            arr2 = createArrayDesc(7000)
            arr = np.concatenate([arr1, arr2])
            for algo in Algos:
                print(algo.name)
                arr_copy = arr.copy()
                t0 = time.time()
                if algo != Algos.radixSort:
                    sort(algo, samples[sample_], arr_copy)
                else:
                    arr_copy = radix(arr_copy, __get_num_digits(arr_copy))
                t1 = time.time()
                tot_time = t1 - t0
                timesHR[algo.name][ranges[range_]].append(tot_time)
                print("range: {} sample: {} - {}".format(ranges[range_], samples[sample_], tot_time))

    save_file("outHALFRANDOM{}".format(i), timesHR)

    #  SORTING  4 HALF RANDOM ARRAY
    for range_ in range(len(ranges)):
        for sample_ in range(len(samples)):
            arr1 = createArray(samples[sample_] // 2 - 3500, 0, ranges[range_])
            arr2 = createArrayDesc(3500)
            arr3 = createArray(samples[sample_] // 2 - 3500, 0, ranges[range_])
            arr4 = createArrayDesc(3500)

            arr = np.concatenate([arr1, arr2, arr3, arr4])
            for algo in Algos:
                print(algo.name)
                arr_copy = arr.copy()
                t0 = time.time()
                if algo != Algos.radixSort:
                    sort(algo, samples[sample_], arr_copy)
                else:
                    arr_copy = radix(arr_copy, __get_num_digits(arr_copy))
                t1 = time.time()
                tot_time = t1 - t0
                times4R[algo.name][ranges[range_]].append(tot_time)
                print("range: {} sample: {} - {}".format(ranges[range_], samples[sample_], tot_time))

    save_file("out4RANDOM{}".format(i), times4R)
