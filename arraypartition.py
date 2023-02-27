def array_partition(nums):
    value = 0
    nums.sort()
    for i in range(0, len(nums), 2):
        value += nums[i]
    return value

nums = [6,2,6,5,1,2]
print(array_partition(nums))

