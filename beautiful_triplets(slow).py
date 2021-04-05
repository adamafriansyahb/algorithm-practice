def beautifulTriplets(d, arr):
    count = 0 
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if ( (arr[i] < arr[j] and arr[j] < arr[k]) and ( arr[j] - arr[i] == d and arr[k] - arr[j] == d) ):
                    count += 1
    
    return count
  
d = 3
arr = [1, 2, 4, 5, 7, 8, 10]
