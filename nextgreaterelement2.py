def next_greater_element(arr):
    size = len(arr)
    next_greater = [-1] * size
    stack = []
    for i in range(2 * len(arr)):
        i = i % size
        while len(stack) > 0 and stack[-1][0] < arr[i]:
            x, idx = stack.pop()
            next_greater[idx] = arr[i]
        stack.append((arr[i], i))
    return next_greater

nums = [1,2,3,2,1]
print(next_greater_element(nums))

