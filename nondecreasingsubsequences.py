nums = [4,6,7,7]

def f(i, j):
    subsequences = [[nums[i]]]

    for k in range(i+1, j+1):
        if nums[i] <= nums[k]:
            start_at_k = f(k, j)
            for seq in start_at_k:
                temp = [nums[i]]
                temp.extend(seq)
                subsequences.append(temp)
    return subsequences

def find_subsequences(i, j):
    response = []
    if i != j:
        for k in range(i, j):
            from_k = f(k,j)
            response.extend(from_k)
    return response

v = find_subsequences(0, len(nums)-1)
print(v)
