def minimumAbsoluteDifference(arr):
    minimum = 2147483647
    
    arr.sort()
    
    for i in range(len(arr)-1):
        difference = abs(arr[i] - arr[i+1])
        minimum = min(minimum, difference)
                
    return minimum
