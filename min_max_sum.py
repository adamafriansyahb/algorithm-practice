def hehe(arr):
    arr.sort()

    minimum = 0
    maximum = 0

    for i in range(0, len(arr) - 1):
        minimum += arr[i]
        maximum += arr[-i-1]

    print(minimum, maximum)

arr = [1,3,5,7,9]

hehe(arr)
