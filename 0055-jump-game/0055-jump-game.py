class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_ind = 0
        i = 0
        while i < len(nums) and i <= max_ind:
            max_ind = max(max_ind, i + nums[i])
            i += 1
        return max_ind >= len(nums)-1