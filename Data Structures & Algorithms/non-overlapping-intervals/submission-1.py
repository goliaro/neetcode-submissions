class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals,key=lambda x: x[1])
        last_interval=intervals[0]
        remove=0
        for interval in intervals[1:]:
            if interval[0]<last_interval[1]:
                remove+=1
            else:
                last_interval=interval
        return remove