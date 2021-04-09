def how_many_games(p, d, m, s):
    current_price = p
    money_left = s
    games_bought = 0

    if (s >= p):
        while (money_left > 0 and money_left - current_price >= 0):
            money_left -= current_price

            if (current_price - d > m):
                current_price -= d
            else:
                current_price = m

            games_bought += 1

    return games_bought


p = 100
d = 19
m = 1
s = 180

how_many_games(p, d, m, s)
