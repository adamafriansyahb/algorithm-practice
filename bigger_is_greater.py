def bigger_is_greater(w):
    w = list(w)
    i = len(w) - 1

    while i > 0 and w[i] <= w[i-1]:
        i -= 1

    if i <= 0:
        return 'no answer'

    else:
        # pivot will be at index i-1

        j = len(w) - 1

        while w[j] <= w[i-1]:
            j -= 1

        w[i-1], w[j] = w[j], w[i-1]

        w[i:] = sorted(w[i:])

        result = "".join(w)

        return result


w = "fedcbabcd"
print(bigger_is_greater(w))
