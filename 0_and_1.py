# Condition: 1s are on the left side.

def my_func(n):
    arr_1 = [i for i in n if i == '1']
    arr_0 = [i for i in n if i == '0']

    result = "".join(arr_1) + "".join(arr_0)
    print(result)


n = '01010101'

my_func(n)
