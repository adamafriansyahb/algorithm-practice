const beautifulDays = (i, j, k) => {
    let beautifulDaysCounter = 0;

    for (let x = i; x <= j; x++) {
        let reversed = Number(String(x).split("").reverse().join(""));

        if (Math.abs(x - reversed) % k == 0) {
            beautifulDaysCounter++;
        }
    }

    return beautifulDaysCounter;
}

i = 13
j = 45
k = 3

beautifulDays(i, j, k);