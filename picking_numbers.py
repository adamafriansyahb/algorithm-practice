def picking_numbers(a):
    a.sort()
    longest = 0

    for i in range(len(a)):
        desired_arr = []
        
        for j in range(i+1, len(a)):
            if (abs(a[i] - a[j]) <= 1):
                desired_arr.append(a[j])

        if len(desired_arr) > 0:
            desired_arr.append(a[i])

        if len(desired_arr) > longest:
            longest = len(desired_arr)

    return longest

a = [4,6,5,3,3,1] 
print(picking_numbers(a))