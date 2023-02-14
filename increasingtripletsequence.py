def increasing_triplet(nums):
    n = len(nums)

    if n < 3:
        return False

    mini = [0] * n
    maxx = [0] * n
    mini[1], maxx[-2] = (nums[0], nums[1])
    
    for i in range(2, n):
        mini[i] = min(mini[i-1], nums[i-1])

    for i in range(n-2, -1, -1):
        maxx[i] = max(maxx[i+1], nums[i+1])

    for i in range(1,n-1):
        if mini[i] < nums[i] < maxx[i]:
            return True
    return False

increasing_triplet(nums)
