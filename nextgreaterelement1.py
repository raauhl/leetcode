from collections import defaultdict

def next_greater_element(nums):

    next_greater = [-1] * len(nums)
    stack = [(nums[0], 0)] 
    for i in range(1, len(nums)):
        num = nums[i]
        if num < stack[-1][0]:
            stack.append((num, i))
        else:
            while len(stack) > 0 and stack[-1][0] < num:
                x, idx = stack.pop()
                next_greater[idx] = num
            stack.append((num, i))
    return next_greater

def solve(nums1, nums2):
    next_greater = next_greater_element(nums2)
    print(next_greater)

    mapper = defaultdict(int)
    for i, x in enumerate(nums2):
        mapper[x] = i
        
    response = []
    for x in nums1:
        idx = mapper[x]
        response.append(next_greater[idx])
    return response    

nums1 = [4,1,2]
nums2 = [1,3,4,2]
v = solve(nums1, nums2)
print(v)



