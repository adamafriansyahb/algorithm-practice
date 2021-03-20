def socket_merchant(n, ar):
    unique = list(set(ar))
    pairs = []
    for i in unique:
        pair = ar.count(i) // 2
        if pair > 0:
            pairs.append(pair)

    return sum(pairs)

n = 9
ar = [10,20,20,10,10,30,50,10,20,50,50,50,50]
print(socket_merchant(n, ar))
