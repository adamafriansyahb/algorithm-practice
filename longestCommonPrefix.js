// algorithm by Nick White.

const longestCommonPrefix = (arr) => {
    if (arr.length > 0) {  
        let prefix = arr[0];

        for (i=1; i<arr.length; i++) {
            // traverse each string in the array.
            // while current prefix does not exist in current string, drop the last char of the prefix.
            while (arr[i].indexOf(prefix) != 0) {
                prefix = prefix.substr(0, prefix.length-1);
            }
        }
    
        return prefix;
    }
    else { 
        return "";
    }
}

const arr = ['c', 'acc', 'cac'];

const tes = longestCommonPrefix(arr);

console.log(tes);