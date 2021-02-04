// find the first reccuring character using nested loop.

const myFunction = (word) => {
    const string = word.toUpperCase();
    for (let i=0; i<string.length; i++) {
        for (let j=i+1; j<string.length; j++) {
            if (string[i] == string[j]) {
               return string[i];
            }
        }
    }
    return null;
}

console.log(myFunction('KorOEeeE'));