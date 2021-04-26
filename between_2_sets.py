from functools import reduce


def getTotalX(a, b):

    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)

    def lcm(a, b):
        return a*b // gcd(a, b)

    g = reduce(gcd, b)
    l = reduce(lcm, a)

    count = 0
    for i in range(l, g+1, l):
        if g % i == 0:
            count += 1

    return count


a = [2, 4]
b = [16, 32, 96]

print(getTotalX(a, b))
