from random import random, randrange


def heapify(arr, size, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < size and arr[largest] < arr[left]:
        largest = left

    if right < size and arr[largest] < arr[right]:
        largest = right

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, size, largest)


def heapSort(arr):
    size = len(arr)

    for i in range(size // 2 - 1, -1, -1):
        heapify(arr, size, i)

    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


# array = [randrange(10000) for _ in range(1000)]
# print(array)
# heapSort(array)
# print(array)
