def my_function(n):
    shared = 5
    cumulative = 0

    for i in range(n):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
   
    return cumulative

    

n = 5
print(my_function(n))