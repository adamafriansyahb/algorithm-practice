# HackerRank - Problem solving -> Algorithm -> Number line jumps

def kangaroo(x1, v1, x2, v2):
    pos_1 = x1
    pos_2 = x2

    if (x1 < x2 and v1 > v2):
        while pos_1 != pos_2:
            pos_1 += v1
            pos_2 += v2

            if (pos_1 > pos_2):
                return "NO"
                break
        return 'YES'
    elif (x2 < x1 and v2 > v1):
        while pos_1 != pos_2:
            pos_1 += v1
            pos_2 += v2

            if (pos_2 > pos_1):
                return "NO"
                break
        return 'YES'
    elif (x1 == x2 and (v1 > v2 or v2 > v1)):
        return "NO"
    elif (x1 == x2 and v1 == v2):
        return "YES"
    else:
        return "NO"


x1 = 0
v1 = 3
x2 = 4
v2 = 2

print(kangaroo(x1, v1, x2, v2))
