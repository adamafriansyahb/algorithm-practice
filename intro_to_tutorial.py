def introTutorial(V, arr):
    for i in range(len(arr)):
        if V == arr[i]:
            return i


V = 6
arr = [1, 2, 3, 4, 5, 6]

print(introTutorial(V, arr))
