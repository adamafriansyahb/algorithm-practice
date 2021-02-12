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
    let arr = []
    for (let i=0; i<n; i++){
        arr.push(fibonacci(i))
    }

    return arr;
}

console.log(hehe(8))
