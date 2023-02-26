from collections import defaultdict

def mod(a, b):
    if a == 0:
        return 0
    if a > 0:
        return a%b
    

def subarrays_div_by_k(nums, k):

    mapper = defaultdict(int)
    mapper[0] = 1
    prefix_sum = 0
    subarrays = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]
        remainder = prefix_sum % k
        if remainder in mapper:
            subarrays += mapper[remainder]
            mapper[remainder] += 1
        else:
            mapper[remainder] = 1
    
    return subarrays

nums = [4,5,0,-2,-3,1]
k = 5
print(subarrays_div_by_k(nums, k))
