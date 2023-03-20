# https://leetcode.com/problems/palindrome-partitioning-ii/

def cut_is_answer(cut):
    # generates all possibe partitions of the string into cut parts
    pass
    
import sys

def is_palindrome(s):
    i, j = 0, len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def f(s):
    
    if is_palindrome(s):
        return 0

    mini = sys.maxsize
    for i in range(len(s)-1):
        curr = f(s[:i+1]) + 1 + f(s[i+1:])
        mini = min(mini, curr)
    
    return mini

    
    



