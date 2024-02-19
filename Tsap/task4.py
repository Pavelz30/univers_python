# Option 1 (1)
def func1(n):
    if n == 0:
        return 0.72
    if n == 1:
        return -0.93
    if n >= 2:
        return func1(n-2) ** 2 + func1(n - 2) + \
            func1(n - 1) ** 3 - func1(n-1) ** 3
g