class Solution:
    def longestPalindrome(self, s: str) -> str:
        # maxlen = 0
        # sp = 0
        # n = len(s)
        # dp = [[-1 for i in range(n)] for j in range(n)]
        
        # def ispalindrome(s, i, j):
        #     if i >= j:
        #         return 1
        #     elif dp[i][j] != -1:
        #         return dp[i][j]
        #     elif s[i] == s[j]:
        #         dp[i][j] = ispalindrome(s, i+1, j-1)
        #         return dp[i][j]
        #     else:
        #         return 0
        
        # for i in range(n):
        #     for j in range(n):
        #         if ispalindrome(s, i, j):
        #             if j - i + 1 > maxlen:
        #                 maxlen = j - i + 1
        #                 sp = i
        # return s[sp: sp + maxlen]
        
        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1: j]
        
        longest = ""

        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)

            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even
        return longest
