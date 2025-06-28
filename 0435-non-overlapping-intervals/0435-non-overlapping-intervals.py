class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        count = 0
        prev_int = intervals[0]
        n = len(intervals)
        i = 1
        while i < n:
            if intervals[i][0] < prev_int[1]:
                count += 1
            else:
                prev_int = intervals[i]
            i += 1
        return count