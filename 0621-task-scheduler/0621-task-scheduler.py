class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        hq = []
        for k,v in count.items():
            heapq.heappush(hq, (-v,k))
        time = 0
        while hq:
            tmp  = []
            for i in range(n+1):
                if hq:
                    freq, task = heapq.heappop(hq)
                    freq += 1
                    if freq != 0:
                        tmp.append((freq, task))
                time += 1

                if not hq and not tmp:
                    break
            for item in tmp:
                heapq.heappush(hq, item)
        return time
        