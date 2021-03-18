def my_function(steps, path):
    # Write your code here
    sea_level = 0
    valleys_counter = 0

    for i in range(steps):
        if path[i] == 'U':
            sea_level += 1
        else:
            sea_level -= 1

        if sea_level == 0 and path[i] == 'U':
            valleys_counter += 1

    return valleys_counter

steps = 12
path = 'DDUUDDUDUUUD'

print(my_function(steps, path))