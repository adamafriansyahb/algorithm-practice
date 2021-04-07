import math


def kaprekar_numbers(p, q):
    result = []
    for i in range(p, q+1):
        x = str(i * i)
        d = math.ceil(len(x) / 2)

        right = (x[(-1*d):])

        if (len(x) < 2):
            left = 0
        else:
            left = (x[:len(x) // 2])

        if (int(left) + int(right) == i):
            result.append(str(i))

    if len(result) > 0:
        print(" ".join(result))
    else:
        print('INVALID RANGE')


kaprekar_numbers(1, 99999)
