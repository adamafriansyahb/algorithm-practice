const jumpingOnClouds = (c) => {
    let jumps = 0
    let i = 0
    
    while (i < c.length - 1) {
        if (c[i] == 0) {
            i += 2
        } else {
            i += 1
        }
        jumps++
    }

    return jumps
}

