def jumping_on_clouds(c, k):
    energy = 100
    i = 0
    begin = True

    while(begin):
        jump_to = (i + k) % len(c)
        current = c[jump_to]
        
        if current == 0:
            energy -= 1
        else:
            energy -= 3

        i = jump_to

        if i == 0:
            begin = False

    return energy

k = 2
c = [0,0,1,0,0,1,1,0]

print(jumping_on_clouds(c, k))