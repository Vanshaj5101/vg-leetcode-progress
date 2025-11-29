class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        hshmap = defaultdict(int)
        for n in nums:
            hshmap[n] += 1
        
        heap = list(hshmap.keys())
        heapq.heapify(heap)

        while heap:
            first = heap[0]
            for i in range(first, first+k):
                if i not in hshmap:
                    return False
                hshmap[i] -= 1
                if hshmap[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)
        return True
                

