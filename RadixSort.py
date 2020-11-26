from functools import reduce


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

