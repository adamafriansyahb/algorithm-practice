const equalizeArray = (arr) => {
    let dict = {};
    
    for (let i=0; i<arr.length; i++) {
        if (!(arr[i] in dict)) {
            dict[arr[i]] = 1;
        } else {
            dict[arr[i]] += 1;
        }
    }

    const counts = Object.values(dict);
  
    return arr.length - Math.max(...counts);
}

arr = [1,2,2,2,1,3,3,4,5,4,5,6,7,6,7];
console.log(equalizeArray(arr));