def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    
	total = 0
    
    for i in range(len(calorie)):
        total += (2 ** i) * calorie[i]
    
    return total
