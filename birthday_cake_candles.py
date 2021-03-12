def my_function(candles):
    candles.sort(reverse=True)
    tallest = candles[0]
    tallest_counter = 1

    for i in range(1, len(candles)):
        if candles[i] == tallest:
            tallest_counter += 1

    return tallest_counter
    

candles = [5,4,2,7,5,6,7,5,7,3]
print(my_function(candles))