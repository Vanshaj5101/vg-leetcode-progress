class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        min_len = float('inf')
        window_sum = 0
        for right in range(n):
            window_sum += nums[right]
            while window_sum >= target:
                min_len = min(min_len, right-left + 1)
                window_sum -= nums[left]
                left += 1
        return min_len if min_len != float('inf') else 0
                