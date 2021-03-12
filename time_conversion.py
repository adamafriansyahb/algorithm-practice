def result(hour, minute, second):
    return hour + ':' + minute + ':' + second

def my_function(s):
    x = s.split(':')
    y = list(x[2])

    hour = int(x[0])
    minute = x[1]
    second = y[0] + y[1]
    determiner = y[2]

    if (determiner == 'P'):
        if (hour == 12):
            hour = str(hour)
            
            return result(hour, minute, second)
        else:
            hour += 12
            hour = str(hour)
            
            return result(hour, minute, second)

    elif (determiner == 'A'):
        if (hour == 12):
            hour -= 12

        if (hour < 10):
            hour = '0' + str(hour)
        else:
            hour = str(hour)

        return result(hour, minute, second)

s = '12:45:54PM'
print(my_function(s))