def assign_cookies(g, s):
            
    x, y = -1, 0

    g.sort()
    s.sort()
    while y != len(s) and x != len(g)-1:
        while y < len(s) and s[y] < g[x+1]:
            y += 1
        if y == len(s):
            break
        x += 1
        y += 1
        
    return x+1

g = [1,2]
s = [1,2,3]

print(assign_cookies(g, s))

