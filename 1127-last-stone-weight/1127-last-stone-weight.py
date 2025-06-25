class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            w = 0 if s1 == s2 else abs(abs(s1) - abs(s2))
            if w:
                heapq.heappush(stones, -w)
        
        return -stones[0] if stones else 0