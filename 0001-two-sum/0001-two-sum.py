class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsh = dict()
        for i in range(len(nums)):
            if target - nums[i] in hsh:
                return [hsh[target - nums[i]], i]
            hsh[nums[i]] = i
