class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-w for w in stones]
        heapq.heapify(heap)
        while heap and len(heap) != 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, -(y-x))
        return abs(heap[0]) if heap else 0