# HackerRank: Problem Solving -> Day of the Programmer

def dayOfProgrammer(year):

    if (year >= 1700 and year <= 1917):
        leap_year = True if (year % 4 == 0) else False

    elif (year == 1918):
        return("26.09.{year}".format(year=year))

    else:
        leap_year = True if (year % 400 == 0 or (
            year % 4 == 0 and year % 100 != 0)) else False

    if (leap_year):
        return("12.09.{year}".format(year=year))
    else:
        return("13.09.{year}".format(year=year))


print(dayOfProgrammer(1984))
