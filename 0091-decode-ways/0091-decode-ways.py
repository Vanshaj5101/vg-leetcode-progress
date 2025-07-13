class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1  # Base case: empty string has 1 valid decoding

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0  # '0' can't be decoded
            else:
                dp[i] = dp[i + 1]  # Single digit

                if i + 1 < n and 10 <= int(s[i:i + 2]) <= 26:
                    dp[i] += dp[i + 2]  # Two digits

        return dp[0]