from collections import defaultdict

def total_fruits(fruits):

    mapper = defaultdict(int)
    mapper[fruits[0]] = 0

    for i in range(1, len(fruits)):
        

