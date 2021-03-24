def taumBday(b, w, bc, wc, z):

    min_cost = bc if bc <= wc else wc
    convert_item = w if bc <= wc else b

    res_1 = (bc * b) + (wc * w)
    res_2 = (min_cost * b) + (min_cost * w) + (z * convert_item)
    result = min(res_1, res_2)

    return min(res_1, res_2)


b = 542
w = 296
bc = 159324
wc = 460882
z = 418824

print(taumBday(b, w, bc, wc, z))
