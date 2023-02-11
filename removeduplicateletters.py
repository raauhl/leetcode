from collections import defaultdict

def remove_duplicate_letters(s):
    counter = defaultdict(int)
    seen = set()
    stack = []

    for ch in s:
        counter[ch] += 1
    
    for ch in s:
        if ch in seen:
            counter[ch] -= 1
            continue

        while len(stack) > 0 and stack[-1] > ch and counter[stack[-1]] > 0:
            seen.remove(stack[-1])
            stack.pop()

        stack.append(ch)
        seen.add(ch)
        counter[ch] -= 1
    
    return ''.join(stack)

s = 'bcabc'
answer = remove_duplicate_letters(s)
print(answer)