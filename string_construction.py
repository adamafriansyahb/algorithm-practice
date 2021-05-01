def stringConstruction(s):
    unique = {}
    cost = 0
    
    for i in s:
        if i not in unique:
            unique[i] = 1
            cost += 1
            
    return cost
