def my_function(s, d, m):
    counter = 0
    bar_sum = 0

    for i in range(len(s)-m+1):
       
        for j in range(i, i+m):
            bar_sum += s[j]

        if bar_sum == d: counter += 1

        bar_sum = 0

    return counter

s = [4]
d = 4
m = 1

print(my_function(s, d, m))