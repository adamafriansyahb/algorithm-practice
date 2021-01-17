const isPalindrome = (num) => {
    num = String(num);
    rev = num.split("").reverse().join("");
    
    if (rev === num) {
        return true;
    } 
    else {
        return false;
    }
}

tes = check(-101);
console.log(tes);