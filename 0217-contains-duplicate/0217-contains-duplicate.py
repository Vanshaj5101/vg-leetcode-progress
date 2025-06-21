class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hshset = set()
        for n in nums:
            if n in hshset:
                return True
            hshset.add(n)
        return False