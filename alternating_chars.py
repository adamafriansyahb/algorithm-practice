def alternatingCharacters(s):
    delete = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            delete += 1
            
    return delete
