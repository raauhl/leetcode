

def increasing_triplet(nums):
    if len(nums) < 3:
        return False

    n = len(nums)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                print(i, j, k)

nums = [1,2,3,4,5]
increasing_triplet(nums)
