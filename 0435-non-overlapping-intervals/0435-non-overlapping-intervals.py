class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x:x[0])
        remove = 0
        prev = intervals[0][1]
        i = 1
        
        while i < n:
            if intervals[i][0] >= prev:
                prev = intervals[i][1]
            else:
                remove += 1
                prev = min(intervals[i][1], prev)
            i += 1
        
        return remove