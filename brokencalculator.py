def broken_calc(start_value, target):

    if start_value >= target:
        return target - start_value
    
    if target%2 == 0:
        return 1 + broken_calc(start_value, target // 2)
        
    return 1 + broken_calc(start_value, target // 2)
    


start_value = 3
target = 10

print(broken_calc(start_value, target))