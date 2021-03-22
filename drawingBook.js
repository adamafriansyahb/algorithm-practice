const pageCount = (n, p) => {
    const front = Math.floor(p / 2);
    const back = (n % 2 == 0) ? Math.floor((n-p+1) / 2) : Math.floor((n-p) /2);

    return Math.min(front, back);
}

n = 5;
p = 3;

console.log(pageCount(n, p));