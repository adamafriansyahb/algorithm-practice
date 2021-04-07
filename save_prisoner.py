def saveThePrisoner(n, m, s):
    from_seat_s = ((m % n) + s - 1) % n

    return n if from_seat_s == 0 else from_seat_s


n = 7
m = 19
s = 2

print(saveThePrisoner(n, m, s))
