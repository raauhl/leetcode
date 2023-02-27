from collections import defaultdict

def min_window_1(s, t):

    m = len(s)
    n = len(t)
    substring = ""

    mapper = defaultdict(int)
    for ch in t:
        mapper[ch] += 1

    for i in range(m-n+1):
        t_mapper = mapper.copy()
        print(s[i:m])
        for j in range(i, m):
            ch = s[j]
            if ch in t_mapper:
                t_mapper[ch] -= 1
                if t_mapper[ch] == 0:
                    del t_mapper[ch]
            if len(t_mapper) == 0 and (j-i+1 < len(substring) or substring == ""):
                substring = s[i:j+1]

    return substring


def min_window(s, t):

    m = len(s)
    n = len(t)

    mapper = defaultdict(int)
    for ch in t:
        mapper[ch] += 1


    i = 0
    seen = False

#    Seen  chr
#    True  True    =>  reduce map
#    True  False   =>  continue
#    False True    =>  seen=True, reduce map
#    False False   =>  continue

    window = defaultdict(int)

    while i < m-n+1:

        if s[i] in mapper:
            j = i
            while True:
                if window == mapper:
                    break
                window[s[j]] += 1

    def equals(window, t_map):

        lower = []
        for i in range(26):
            lower.append()
            
            

        
            



        
    



s = "ADOBECODEBANC"
t = "ABC"

print(min_window(s, t))