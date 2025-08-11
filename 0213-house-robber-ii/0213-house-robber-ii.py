class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        else:
            def min_cost(costs):
                l = len(costs)
                dp = [0] * l
                dp[0] = costs[0]
                dp[1] = max(costs[0], costs[1])
                for i in range(2, l):
                    dp[i] = max(dp[i-2] + costs[i], dp[i-1])
                return dp[l-1]
            
            return max(min_cost(nums[0:n-1]), min_cost(nums[1:n]))
