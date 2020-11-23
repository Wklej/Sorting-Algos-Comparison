import random
import numpy
import time

def partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while (True):
        i+=1
        while (arr[i] < pivot):
            i += 1

        j-=1
        while (arr[j] > pivot):
            j -= 1

        if (i >= j):
            return j

        arr[i], arr[j] = arr[j], arr[i]  # swapping


def quickSort(arr, low, high):
    if (low < high):
        pi = partition(arr, low, high)
        quickSort(arr, low, pi)
        quickSort(arr, pi + 1, high)


#
# n = [500000]
# times = {'quick': []}
# samples = len(n)
#
# for size in n:
#     tot_time = 0
#     for _ in range(samples):
#         a = createarray(size, 0, size)
#         t0 = time.time()
#         quickSort(a, 0, size - 1)
#         t1 = time.time()
#         tot_time = (t1 - t0)
#     times['quick'].append(tot_time) #/float(samples)
#
# print("n\tQuicksort")
# print(40*"_")
# for i, size in enumerate(n):
#     print("%d\t %0.5f"%(
#         size,
#         times['quick'][i]
#     ))

