# Passed 9/10 test cases on HackerRank.
# 1 test case didn't pass because it exceeded the time limit

def rotate_left(d, arr):
    for i in range(d):

        body = arr[1:]
        body.append(arr[0])

        arr = body

    return body


d = 2
arr = [5, 4, 3, 2, 1, 0]

print(rotate_left(d, arr))
