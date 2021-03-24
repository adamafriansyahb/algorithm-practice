const reverseArray = (a) => {
    let arr = [];
    for (let i=a.length-1; i>=0; i--) {
        arr.push(a[i]);
    }

    return arr;
}

a = [1,4,3,2]
console.log(reverseArray(a));