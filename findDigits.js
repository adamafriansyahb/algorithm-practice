const findDigits = (n) => {
    const numbers = n.toString();
    let counter = 0;

    for (let i=0; i<numbers.length; i++) {
        if ( Number(numbers[i]) !== 0 && n % Number(numbers[i]) == 0 ) {
            counter++;
        }
    }

    return counter;
}

n = 124
console.log(findDigits(n));