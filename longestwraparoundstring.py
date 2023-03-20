from collections import defaultdict 

def f(s):
    def order(ch):
        return (ord(ch) - ord('a'))

    mapper = defaultdict(int)
    mapper[s[0]] = curr_length = 1
    for i in range(1, len(s)):
        if (order(s[i-1]) + 1) % 26 == order(s[i]):
            curr_length += 1
        else:
            curr_length = 1
        mapper[s[i]] = max(mapper[s[i]], curr_length)
    return sum(mapper.values())


