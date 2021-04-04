def my_func(n, a, b):
    highest = a if a > b else b
    lowest = a if a < b else b

    nearest = (n - 1) * lowest

    result = set()

    for _ in range(n):
        result.add(nearest)
        nearest += (highest - lowest)

    return sorted(list(result))


n = 4
a = 10
b = 100

print(my_func(n, a, b))
