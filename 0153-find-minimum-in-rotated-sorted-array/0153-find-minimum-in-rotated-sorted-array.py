class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        min_num = nums[0]
        while l<=r:
            mid = (r + l) // 2
            min_num = min(min_num, nums[mid])
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
            
        return min_num