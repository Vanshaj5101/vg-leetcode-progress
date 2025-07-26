class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hshmap = dict()
        for i in range(len(nums)):
            if target - nums[i] in hshmap:
                return [i, hshmap[target - nums[i]]]
            hshmap[nums[i]] = i
        