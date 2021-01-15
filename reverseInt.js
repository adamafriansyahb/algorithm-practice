const upperBound = 2**31;
const lowerBound = upperBound * -1;

const reverse = (num) => {
    let result = String(Math.abs(num)).split("");
    result = result.reverse().join("");
    result = Number(result);
        
    if (num < 0) {
        result = result * -1;
        if (result >= lowerBound && result <= upperBound) {
            return result;
        } 
        else {
            return 0;
        }
    } 
    else {
        if (result >= lowerBound && result <= upperBound) {
            return result;
        } 
        else {
            return 0;
        }
    }

}

console.log(reverse(-1534236469)); 
