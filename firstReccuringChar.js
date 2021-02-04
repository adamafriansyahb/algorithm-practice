const firstReccuringChar = (str) => {
    let hehe = {};
    const string = str.toUpperCase();
    
    for (let i = 0; i<string.length; i++) {
        // check whether or not current char is already in the dict.
        if (!(string[i] in hehe)){
            hehe[string[i]] = 1
        }
        else {
            return string[i];
        }
    }
    // if there is no reccuring character in a given string, return null.
    return null;
}

console.log(firstReccuringChar('kAmoE CanTyK'));
