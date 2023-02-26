nums = [4,5,2,1]
queries = [3,10,21]

def last_smaller_number(q, prefix_sum):
    i, j = 0, len(prefix_sum)-1
    while i <= j:
        mid = (i+j) // 2
        if q < prefix_sum[mid]:
            j = mid-1
        else:
            i = mid+1
    return (j+1)
        

def longest_subsequence_with_limited_sum():
    
    response = []
    prefix_sum = []
    value = 0
    nums.sort()
    for n in nums:
        value += n
        prefix_sum.append(value)
    for q in queries:
        response.append(last_smaller_number(q, prefix_sum))
    return response

print(longest_subsequence_with_limited_sum())