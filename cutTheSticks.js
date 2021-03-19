const cutTheSticks = (arr) => {
    let numOfSticks = [];
    
    while (arr.length) {
        numOfSticks.push(arr.length);
        let min = Math.min(...arr);
        // console.log(`Min: ${min}`);
        // console.log(`Prev: ${arr}`);

        for (let j=0; j<arr.length; j++) {
            arr[j] -= min;
            if (arr[j] === 0) {
                arr.splice(j, 1);
                j--;
            }
        }
        
        // console.log(`Current: ${arr}`);
        // console.log('--------------------'); 
    }

    return numOfSticks;
}

arr = [5,4,4,2,2,8]
console.log(cutTheSticks(arr));
