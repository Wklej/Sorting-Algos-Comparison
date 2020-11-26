from functools import reduce
import time
import numpy as np
import random


def __get_num_digits(A):
    m = 0  # max number of digits
    for item in A:
        m = max(item, m)  # compare item to m
    return len(str(m))


def __flatten(bucket):
    return reduce(lambda x, y: x + y, bucket)


def radix(A, num_of_digits):
    for digit in range(0, num_of_digits):
        bucket = [[] for _ in range(10)]  # creating 10 empty lists
        for item in A:
            num = item // 10 ** digit % 10  # // - adjusted to the left(3.75 = 3), ** - power of, %10 (ostatnia cyfra)
            bucket[num].append(item)
        A = __flatten(bucket)
    return A


# def main():
#     A = [random.randrange(0, 10000) for _ in range(10000)]
#     B = A.copy()
#     #print(A)
#     num_of_digits = __get_num_digits(A)
#     t0 = time.time()
#     B = radix(B, __get_num_digits(B))
#     t1 = time.time()
#     #print(A)
#     tot_time = t1 - t0
#     print(B[:5], B[-5:])
#     print(tot_time)


#
#main()
