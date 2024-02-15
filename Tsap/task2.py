
def func1(z):
    if z < 30:
        temp = (2 - 36 * z ** 2 - z) ** 7 / 88 - (1 - z ** 3 - z) ** 5
    elif z >= 76:
        temp = (1 - z ** 2) ** 3
    else:
        temp = (47 * z ** 3 + z) ** 2
    return temp


def func2(z):
    return (2 - 36 * z ** 2 - z) ** 7 / 88 - (1 - z ** 3 - z) ** 5 \
        if z < 30 else (1 - z ** 2) ** 3 if z >= 76 else (47 * z ** 3 + z) ** 2


def func3(z):
    dictionary = {z < 30: (2 - 36 * z ** 2 - z) ** 7 / 88 -
                          (1 - z ** 3 - z) ** 5,
                  z >= 76: (1 - z ** 2) ** 3,
                  30 <= z < 76: (47 * z ** 3 + z) ** 2}
    return dictionary[True]
