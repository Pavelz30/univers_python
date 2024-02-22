import math

# Option 1


def func1(n, m, b):
    res = 0
    for k in range(1, b + 1):
        for i in range(1, m + 1):
            for c in range(1, n + 1):
                res += (65 * math.tan(c) + math.pow(math.sin(i), 7) + k ** 4)
    return res

# Option 2


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

# Option 3


def func3(n, m, b):
    matrix = [(65 * math.tan(c) + math.pow(math.sin(i), 7) + k ** 4)
              for c in range(1, n + 1) for i in range(1, m + 1)
              for k in range(1, b + 1)]
    return sum(matrix)

# Option 4


def func4(n, m, b):
    matrix = ((65 * math.tan(c) + math.pow(math.sin(i), 7) + k ** 4)
              for c in range(1, n + 1) for i in range(1, m + 1)
              for k in range(1, b + 1))
    return sum(matrix)

# Option 5


def f2(n, m, b):
    if n == 0:
        return 0
    return 65 * math.tan(n) + math.pow(math.sin(m), 7) \
        + b ** 4 + f2(n - 1, m, b)


def f1(n, m, b):
    if m == 0:
        return 0
    return f2(n, m, b) + f1(n, m - 1, b)


def main(n, m, b):
    if b == 0:
        return 0
    return f1(n, m, b) + main(n, m, b - 1)


print(main(7, 3, 2))
