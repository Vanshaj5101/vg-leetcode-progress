class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(i, j):
            count = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                count += 1
            return count
        
        total = 0

        for i in range(len(s)):
            total += expand(i, i)
            total += expand(i, i+1)
        return total