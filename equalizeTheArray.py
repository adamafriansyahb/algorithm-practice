def equalizeArray(arr):
    hehe = {}
    new_arr = []
    for i in arr:
        if i not in hehe:
            hehe[i] = 1
            new_arr.append(arr.count(i))

    maximum_count = max(new_arr)
    new_arr.sort()
    new_arr.pop()

    return sum(new_arr)


arr = [1, 2, 2, 3]
print(equalizeArray(arr))
