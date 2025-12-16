class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        # dp[i] = num of ways to decode string s from index i to n
        
        dp[n] = 1 # dp[n] = 1 because num of ways to decode string from nth index to n = 1

        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            
            if i + 1 < n:
                if s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"):
                    dp[i] += dp[i+2]
        
        return dp[0]