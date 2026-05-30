class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        asn = -1
        count = 0
        for n in nums:
            if not count:
                ans = n
            
            if n == ans:
                count += 1
            else:
                count -= 1
        return ans