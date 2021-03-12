def my_function(scores):
    highest = scores[0]
    lowest = scores[0]

    highest_counter = 0
    lowest_counter = 0

    for i in range(1, len(scores)):
        if (scores[i] > highest):
            highest = scores[i]
            highest_counter += 1
        elif (scores[i] < lowest):
            lowest = scores[i]
            lowest_counter += 1

    return [highest_counter, lowest_counter]

scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
print(my_function(scores))