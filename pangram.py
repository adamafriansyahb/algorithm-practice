def pangrams(s):

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']

    count = 0

    for i in alphabet:
        if i in s.lower():
            count += 1

    return 'pangram' if count == len(alphabet) else 'not pangram'
