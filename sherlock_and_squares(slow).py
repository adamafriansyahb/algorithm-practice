def my_function(a, b):
    counter = 0
    for i in range(a, b+1):
        square_root = i ** (1/2)
        if square_root.is_integer():
            counter += 1

    return counter


a = 24
b = 49

print(my_function(a, b))
