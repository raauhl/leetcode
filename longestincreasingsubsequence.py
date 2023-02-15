def length_of_lis(nums):

    prev = [None] * len(nums)
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i] and dp[j]+1 > dp[i]:
                dp[i] = dp[j]+1
                prev[i] = j

    index = dp.index(max(dp))
    lis = [nums[index]]
    while prev[index] != None:
        index = prev[index]
        lis.append(nums[index])
    print(lis)
    
nums = [10,9,2,5,3,7,101,18]
length_of_lis(nums)