# Convert the multiplication of two integers into binary, then find the amont of 1s in binary.

def my_func(a, b):
    arr = []
    n = a * b

    while n != 0:
        arr.append(n % 2)
        n = n // 2

    arr.reverse()

    return arr.count(1)


print(my_func(3, 7))
