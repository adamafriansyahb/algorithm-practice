def chocolateFeast(n, c, m):
    temp = choco = n // c
    while temp >= m:
        choco += temp // m
        temp = (temp // m) + (temp % m)

    return choco


n = 10
c = 2
m = 5

print(chocolateFeast(n, c, m))
