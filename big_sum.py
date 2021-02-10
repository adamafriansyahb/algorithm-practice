def sum_array(a):
    if (len(a) > 10):
        return

    result = 0
    for i in range(len(a)):
        if (a[i] > 10**10):
            return
        
        result += a[i]

    return result

a = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

print(sum_array(a))
