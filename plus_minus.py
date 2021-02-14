def plusMinus(arr):
    zero = []
    positive = []
    negative = []

    for i in arr:
        if (i == 0):
            zero.append(i)
        elif (i < 0):
            negative.append(i)
        else:
            positive.append(i)

    ratio_positive = format(len(positive) / len(arr), '.6f')
    ratio_negative = format(len(negative) / len(arr), '.6f')
    ratio_zero = format(len(zero) / len(arr), '.6f')

    print(ratio_positive)
    print(ratio_negative)
    print(ratio_zero)

arr = [1,1,0,-1,-1]

plusMinus(arr)