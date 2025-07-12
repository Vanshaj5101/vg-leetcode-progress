class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n==2:
            return max(nums[0], nums[1])
        
        # n[0:n-2]
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        for i in range(2, n-1):
            curr = max(prev2 + nums[i], prev1)
            prev2 = prev1
            prev1 = curr
        
        result1 = prev1

        prev2 = nums[1]
        prev1 = max(nums[1], nums[2])
        for i in range(3, n):
            curr = max(prev2 + nums[i], prev1)
            prev2 = prev1
            prev1 = curr
        result2 = prev1

        return max(result1, result2)