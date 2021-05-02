def anagram(s):
    if len(s) % 2 != 0:
        return -1

    s = list(s)
    half = len(s) // 2
    s1 = s[:half]
    s2 = s[half:]

    visited = []
    same_char = 0
    for i in s2:
        s1_count = s1.count(i)
        s2_count = s2.count(i)

        if i not in visited:
            if s2_count == s1_count:
                same_char += s2_count
                visited.append(i)

            elif s1.count(i) != 0 and s1.count(i) != s2.count(i):
                same_char += min(s2_count, s1_count)
                visited.append(i)

            else:
                visited.append(i)

    return half - same_char
