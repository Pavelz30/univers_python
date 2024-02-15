from math import ceil


def main(y):
    temp = 46 - y - (16 * (77 - 50 * y * y - 2 * y) ** 3 -
                     ceil(y - 64 - y ** 2) ** 6) / 12 / y ** 6
    return temp


print(main(-0.12))
