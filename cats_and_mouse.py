def my_function(x, y, z):
    a_to_mouse = abs(z-x)
    b_to_mouse = abs(z-y)

    if (a_to_mouse < b_to_mouse):
        return('Cat A')
    elif (a_to_mouse > b_to_mouse):
        return('Cat B')
    else:
        return('Mouse C')

x = 4
y = 5
z = 3

print(my_function(x, y, x))