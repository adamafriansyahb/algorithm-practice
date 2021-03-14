def my_function(k, height):
    height.sort(reverse=True)

    highest_hurdle = height[0]

    if (highest_hurdle <= k):
        return 0
    else:
        return highest_hurdle - k

k = 4
height = [1,6,3,5,2]

print(my_function(k, height))