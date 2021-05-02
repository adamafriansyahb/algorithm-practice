def anagram(s):
    if len(s) % 2 != 0:
        return -1

    half = len(s) // 2

    difference = Counter(s[:half]) - Counter(s[half:])

    return sum(difference.values())
