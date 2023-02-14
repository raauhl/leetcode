# Given a source string change it to destinations string using minimum number of swaps
# only adjacent characters can be exchanged.

def minimum_swaps(source, destin):

    s = list(source)
    d = list(destin)

    counter = 0
    for i in range(len(s)):
        if s[i] != d[i]:
            idx = s.index(d[i])
            for j in range(idx, i, -1):
                temp = s[j]
                s[j] = s[j-1]
                s[j-1] = temp
                counter += 1
            print(s)
    print(counter)
    
source = '76590'
destin = '90756'

minimum_swaps(source, destin)