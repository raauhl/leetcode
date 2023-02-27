def find_errors_num(nums):

    x = y = None
    nums_set = set()
    for n in nums:
        if n in nums_set:
            x = n
        nums_set.add(n)

    for i in range(1, len(nums)+1):
        if i not in nums_set:
            y = i
    return [x, y]

nums = [1,2,2,4]
print(find_errors_num(nums))


# You have a set of integers s, which originally contains all the numbers from 1 to n. 
# Unfortunately, due to some error, one of the numbers in s got duplicated to another 
# number in the set, which results in repetition of one number and loss of another number.
# You are given an integer array nums representing the data status of this set after the error.
# Find the number that occurs twice and the number that is missing and return them in the
# form of an array.

 
# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]