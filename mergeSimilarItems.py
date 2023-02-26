from collections import defaultdict

def merge_similar_items(items1, items2):
    
    response = []
    mapper = defaultdict(int)

    for value, weight in items1:
        mapper[value] += weight
    for value, weight in items2:
        mapper[value] += weight
    for key in mapper.keys():
        response.append([key, mapper[key]])
    response.sort(key=lambda x: x[0])
    
    return response

items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]
print(merge_similar_items(items1, items2))