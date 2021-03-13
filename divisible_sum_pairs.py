def my_function(n, k, ar):
    counter = 0
    for i in range(n):
        for j in range(i+1, n):
            # print(ar[i], '+', ar[j])
            if (ar[i] + ar[j]) % k == 0:
                counter += 1

    return counter

n = 6
k = 3
ar = [1,3,2,6,1,2]

print(my_function(n, k, ar))