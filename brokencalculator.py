def broken_calc(start_value, target):

    if start_value == target:
        return 0

    if start_value*2 == target:
        return 1

    if start_value-1 == target:
        return 1

    minus = 1 + broken_calc(start_value-1, target)
    if start_value > target:
        return minus
    
    prod = 1 + broken_calc(start_value*2, target)
    return min(minus, prod)
    


start_value = 3
target = 10

print(broken_calc(start_value, target))