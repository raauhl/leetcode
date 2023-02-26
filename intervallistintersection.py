def merge(f, s):
    if f[0] == s[0]:
        return [f[0], min(f[1], s[1])]
    if f[0] > s[0]:
        f, s = s, f
    if f[1] < s[0]:
        return []
    return [max(f[0], s[0]), min(f[1], s[1])]

def interval_intersection(first_list, second_list):
    merged = []
    j = 0
    for f in first_list



    return merged

firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
interval_intersection(first_list=firstList, second_list=secondList)

