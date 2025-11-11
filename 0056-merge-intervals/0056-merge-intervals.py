class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 1:
            return intervals
        
        intervals.sort(key=lambda x:x[0])
        merged = [intervals[0]] 
        for i in range(n):
            if intervals[i][0] <= merged[-1][1]:
                last_interval = merged.pop() 
                merged.append([min(last_interval[0], intervals[i][0]), max(last_interval[1], intervals[i][1])])
            else:
                merged.append(intervals[i])
        
        return merged
                

       