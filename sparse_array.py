def matching_strings(strings, queries):
    count_string = [strings.count(i) for i in queries]

    return count_string


strings = ['aba', 'baba', 'aba', 'xzxb']
queries = ['aba', 'xzxb', 'ab']

print(matching_strings(strings, queries))
