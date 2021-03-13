def my_function(bill, k, b):
    total = 0

    for i in range(len(bill)):
        total += bill[i]

    paid = (total - bill[k]) / 2

    if paid == b:
        return('Bon Appetit')
    else:
        return(int(b - paid)) 

bill = [3,10,2,9]
k = 1
b = 12

print(my_function(bill, k, b))