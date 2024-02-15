import math


def func1(n, m, b):
    res = 0
    for k in range(1, b + 1):
        for i in range(1, m + 1):
            for c in range(1, n + 1):
                res += (65 * math.tan(c) + math.pow(math.sin(i), 7) + k ** 4)
    return res


def func2(n, m, b):
    res = 0
    k, i, c = 1, 1, 1

    while k < b + 1:
        while i < m + 1:
            while c < n + 1:
                res += (65 * math.tan(c) + math.pow(math.sin(i), 7) + k ** 4)
                c += 1
            c = 1
            i += 1
        i = 1
        k += 1
    return res


def func3(n, m, b):
    matrix = [(65 * math.tan(c) + math.pow(math.sin(i), 7) + k ** 4)
              for c in range(1, n + 1) for i in range(1, m + 1)
              for k in range(1, b + 1)]
    return sum(matrix)


def func4(n, m, b):
    matrix = ((65 * math.tan(c) + math.pow(math.sin(i), 7) + k ** 4)
              for c in range(1, n + 1) for i in range(1, m + 1)
              for k in range(1, b + 1))
    return sum(matrix)

