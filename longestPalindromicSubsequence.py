from collections import defaultdict

def longestPalindromeSubseq(self, s: str) -> int:

    cache = defaultdict(int)

    def longest_palindromic_subsequence(i, j):

        if (i,j) in cache:
            return cache[(i,j)]

        if i > j:
            cache[(i,j)] = 0
            return 0

        if i == j:
            cache[(i,j)] = 1
            return 1

        k = j
        while k > i:
            if s[k] == s[i]:
                break
            k -= 1
        
        i_not_taken = longest_palindromic_subsequence(i+1, j)

        if k > i:
            i_taken = longest_palindromic_subsequence(i+1, k-1)
            cache[(i,j)] = max(i_taken+2, i_not_taken)
            return cache[(i,j)]
        
        cache[(i,j)] = i_not_taken
        return i_not_taken  

    v = longest_palindromic_subsequence(0, len(s)-1)
    return v