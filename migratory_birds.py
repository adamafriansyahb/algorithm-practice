def my_function(arr):
    birds = {}
    smallest = 999999

    for i in arr:
        if (i not in birds):
            birds[i] = 1
        else:
            birds[i] += 1

    types = list(birds.keys())
    freq = list(birds.values())
    zipped = tuple(zip(types, freq))

    most_frequent = sorted(freq)[-1]

    for i in range(len(zipped)):
        if (zipped[i][1] == most_frequent):
            if zipped[i][0] < smallest:
                smallest = zipped[i][0]

    return smallest
   


arr = [1,2,3,4,5,4,3,2,1,3,4]

my_function(arr)