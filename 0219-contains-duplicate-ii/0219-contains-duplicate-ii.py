class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hshmap = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in hshmap:
                if abs(hshmap[nums[i]] - i) <= k:
                    return True
            hshmap[nums[i]] = i
        return False
                 