# Given 'n' as number of dices. Return count of all the unique dice rolls.


def f(n):
    arr = set()
    for i in range(1, 7):
        arr.add(tuple([i]))
    
    for i in range(2, n+1):
        new_set = set()
        for item in arr:
            for j in range(1, 7):
                temp = list(item)
                temp.append(j)
                temp.sort()
                new_set.add(tuple(temp))
        arr = new_set
    return len(arr)