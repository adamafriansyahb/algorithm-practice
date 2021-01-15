
const value = (r) => {
    if (r == "I") {
        return 1;
    }
    if (r == "V") {
        return 5;
    }
    if (r == "X") {
        return 10;
    }
    if (r == "L") {
        return 50;
    }
    if (r == "C") {
        return 100;
    }
    if (r == "D") {
        return 500;
    }
    if (r == "M") {
        return 1000;
    }
}

const convert = (r) => {

    let result = 0;

    for (i=0; i<r.length; i++){
        
        if (i + 1 < r.length) {
            if (value(r[i]) < value(r[i+1])) {
                result = result - value(r[i]) + value(r[i+1]);
                i++;
            }
            else {
                result = result + value(r[i]);
            }
        }
        else {
            result = result + value(r[i]);
        }
    }

    return result;
}

tes = "XLIII"
console.log(convert(tes));
