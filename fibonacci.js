function fibonacci(n) {
    let nth;
    if (n==0) {
        return 0;
    }
    else if (n == 1) {
        return 1;
    }
    else {
        nth = fibonacci(n-1) + fibonacci(n-2);
        return nth
    }
}

function hehe(n){
    let counter = 0;
    let arr = []
    for (let i=1; i<=n; i++){
        // console.log(fibonacci(counter));
        arr.push(fibonacci(counter))
        counter++;
    }

    return arr;
}

console.log(hehe(4))