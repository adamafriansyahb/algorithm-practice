const upperBound = 2**31;
const lowerBound = upperBound * -1;

const reverse = (num) => {
    // make the input number into positive, convert it into string, then split.
    let result = String(Math.abs(num)).split("");
    
    // reverse the splitted string, then concatenate them.
    result = result.reverse().join("");
    // revert the string into number.
    result = Number(result);
    
    // check whether the input is positive or negative.
    if (num < 0) {
        // since the input is negative, the returned number must also be negative.
        result = result * -1;
        // check whether it follows the constraints or not.
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

// run the function.
console.log(reverse(-1534236469)); 
