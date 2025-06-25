class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hq = []
        for x,y in points:
            dist = sqrt(pow(x, 2) + pow(y, 2))
            heapq.heappush(hq, (-dist, [x, y]))
        while len(hq) > k:
            heapq.heappop(hq)
        
        res = []
        while hq:
            res.append(heapq.heappop(hq)[1])
        return res
