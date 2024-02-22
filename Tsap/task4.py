# Option 1 (1)
def func1(n):
    if n == 0:
        return 0.72
    if n == 1:
        return -0.93
    if n >= 2:
        return func1(n - 2) ** 2 + func1(n - 2) + \
            func1(n - 1) ** 3 - func1(n - 1) ** 3


# Option 2 (5)
def func2(n):
    return 0.72 if n == 0 else -0.93 if \
        n == 1 else func1(n - 2) ** 2 + func1(n - 2) + \
                    func1(n - 1) ** 3 - func1(n - 1) ** 3 if n >= 2 else 0


# Option 3 (3)
def func3(n):
    arr = [0.72, -0.93]
    for i in range(2, n + 1):
        arr.append(arr[i - 2] ** 2 + arr[i - 2] + arr[i - 1] ** 3 - arr[i - 1] ** 3)
    return arr[-1]


# Option 4 (2)
def func4(n):
    a, b = 0.72, -0.93
    for _ in range(2, n + 1):
        a, b = b, a ** 2 + a + b ** 3 - b ** 3
    return b

# Option 5 (4)
def main(n):
    match n:
        case 0:
            return 0.72
        case 1:
            return -0.93
        case _:
            return func1(n - 2) ** 2 + func1(n - 2)


