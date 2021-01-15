const numerals = [
    {
        name: "M",
        value: 1000
    },
    {
        name: "CM",
        value: 900
    },
    {
        name: "D",
        value: 500
    },
    {
        name: "CD",
        value: 400
    },
    {
        name: "C",
        value: 100
    },
    {
        name: "XC",
        value: 90
    },
    {
        name: "L",
        value: 50
    },
    {
        name: "XL",
        value: 40
    },
    {
        name: "X",
        value: 10
    },
    {
        name: "IX",
        value: 9
    },
    {
        name: "V",
        value: 5
    },
    {
        name: "IV",
        value: 4
    },
    {
        name: "I",
        value: 1
    }
]

const intToRoman = (num) => {
    let result = "";
    let numOfSymbols = 0;

    for (i=0; i<numerals.length; i++) {
        numOfSymbols = parseInt(num / numerals[i].value);
        if (numOfSymbols !== 0) {
            console.log(numOfSymbols);
            for (j=0; j<numOfSymbols; j++){
                result += numerals[i].name;
            }
        }
        num %= numerals[i].value;
    }
    return result;
}

// for (i=0; i<numerals.length; i++) {
//     console.log(numerals[i].value);
// }

const tes = intToRoman(1000);
console.log(tes);


