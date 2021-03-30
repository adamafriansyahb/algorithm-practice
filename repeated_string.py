def repeated_string(s, n):
    arr = list(s)

    count_a = arr.count('a') * (n // len(arr))
    remainder_a = arr[:n % len(arr)].count('a')

    return count_a + remainder_a


s = 'abca'
n = 10

print(repeated_string(s, n))
