def equalizeArray(arr):
    hehe = {}
    new_arr = []
    
    for i in arr:
        if i not in hehe:
            hehe[i] = 1
            new_arr.append(arr.count(i))

    return len(arr) - max(highest)


arr = [1, 2, 2, 3]
print(equalizeArray(arr))
