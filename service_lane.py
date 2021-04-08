# HackerRank - Problem Solving -> Service Lance

def serviceLane(n, cases):
    
    return [min(width[i:j+1]) for i, j in cases]

n = 8
width = [2, 3, 1, 2, 3, 2, 3, 3]
cases = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]

print(serviceLane(n, cases))
