def getLetters():
    char = 'a'

    x = ord(char[0])
    letters = {}

    for i in range(26):
        
        letters[char] = i
        
        x += 1
        char = chr(x)

    return letters

def my_function(h, word):
    letters = getLetters()
    heights = []

    for i in word:
        heights.append(h[letters[i]])
    
    return max(heights) * len(heights)

h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
word = 'zaba'

print(my_function(h, word))