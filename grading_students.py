def my_function(grades):
    for i in range(len(grades)):
        modulus = grades[i] % 5 
        rounded_grade = grades[i] + 5 - modulus
        difference = rounded_grade - grades[i]

        if (grades[i] >= 38):
            if (difference < 3):
                grades[i] = rounded_grade

    return grades

grades = [73, 67, 38, 33]
print(my_function(grades))