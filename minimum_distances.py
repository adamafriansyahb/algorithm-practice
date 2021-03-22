def minimumDistance(a):
    indexes = []
    minimum = 999999
    counter = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                counter += 1
                distance = j - i
                if distance < minimum:
                    minimum = distance

    if counter > 0:
        return minimum
    else:
        return -1

a = [7,1,3,4]
print(minimumDistance(a))