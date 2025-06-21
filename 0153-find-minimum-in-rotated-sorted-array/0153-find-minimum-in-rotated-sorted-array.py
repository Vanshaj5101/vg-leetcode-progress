class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        min_num = nums[0]
        # find_left = 1 if nums[l] < nums[r] else 0
        while l <= r:
            mid = (l + r) // 2
            min_num = min(min_num, nums[mid])
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return min_num
