# Program to multiply two numbers, without using * and / between the two numbers.

def func(x, y):
    total = 0

    if x > 0:
        while (x > 0):
            total += y
            x -= 1

    else:
        while x < 0:
            total -= y
            x += 1

    return total


print(func(-6, -3))
