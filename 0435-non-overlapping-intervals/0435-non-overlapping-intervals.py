class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 1:
            return 0
        
        intervals.sort(key=lambda x:x[0])
        prev = intervals[0][1]
        i = 1
        remove = 0
        while i < n:
            if intervals[i][0] >= prev:
                prev = intervals[i][1]
            else:
                prev = min(intervals[i][1], prev)
                remove += 1
            i += 1
        
        return remove
        

