class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        hshmap = defaultdict(int)
        for n in hand:
            hshmap[n] += 1
        
        heap = list(hshmap.keys())
        heapq.heapify(heap)

        while heap:
            first = heap[0]
            for i in range(first, first + groupSize):
                if i not in hshmap:
                    return False
                hshmap[i] -= 1
                if hshmap[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)
        return True