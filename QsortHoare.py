import sys

sys.setrecursionlimit(1000000)

def partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]  # swapping


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi)
        quickSort(arr, pi + 1, high)

# def quickSort(arr, low, high):
#     while low < high:
#         pi = partition(arr, low, high)
#
#         if pi - low < high - pi:
#             quickSort(arr, low, pi - 1)
#             low = pi + 1
#         else:
#             quickSort(arr, pi + 1, high)
#             high = pi - 1

# def createArrayDesc(elements):
#     arr_desc = np.array([0 for _ in range(elements)])
#     for i in range(elements):
#         arr_desc[i] = elements - i
#     return arr_desc
#
# def createArray(elements, rangefrom, rangeto):
#     return np.array([random.randint(rangefrom, rangeto) for _ in range(elements)])


# size = 3000
# array = createArrayDesc(size)
# array2 = createArray(50000, 0, 1000)
# array3 = np.concatenate((array, array2))
# print(array3)
# quickSort(array3, 0, size - 1)
# print(array3)



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
