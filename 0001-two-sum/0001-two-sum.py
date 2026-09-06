class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hshmap = dict()
        res = []
        for i in range(len(nums)):
            val = target - nums[i]
            if val in hshmap:
                return [hshmap[val], i]
            hshmap[nums[i]] = i
        
        return res

        # TC : O(n)
        # SC : O(n)