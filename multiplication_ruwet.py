# Program to multiply two numbers, without directly using * between the two numbers.

def func(x, y):
    total = 0
    initial_x = x
    if (x < 0):
        x *= -1

    while (x > 0):
        total += y
        x -= 1

    if initial_x < 0:
        return total * -1
    else:
        return total


print(func(-6, -3))
