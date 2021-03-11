def my_function(s, t, a, b, apples, oranges):
    apple_res = []
    orange_res = []
    apple_counter = 0
    orange_counter = 0
    
    if (len(apples) == len(oranges)):
        for i in range(len(apples)):
            apple_from_home = a + apples[i]
            orange_from_home = b + oranges[i]

            apple_res.append(apple_from_home)
            orange_res.append(orange_from_home)

            if (apple_from_home >= s and apple_from_home <= t):
                apple_counter += 1

            if(orange_from_home >= s and orange_from_home <= t):
                orange_counter += 1
    
    else:
        for i in range(len(apples)):
            apple_from_home = a + apples[i]
            apple_res.append(apple_from_home) 
            
            if (apple_from_home >= s and apple_from_home <= t):
                apple_counter += 1       

        for j in range(len(oranges)):
            orange_from_home = b + oranges[j]
            orange_res.append(orange_from_home)

            if(orange_from_home >= s and orange_from_home <= t):
                orange_counter += 1
   
    print(apple_counter)
    print(orange_counter)

s = 7
t = 11
a = 5
b = 15
apples = [-2,2,1]
oranges = [5,-6]

my_function(s, t, a, b, apples, oranges)