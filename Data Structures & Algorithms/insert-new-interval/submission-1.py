class Solution:
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals=[]
        START=0;END=1
        idx=0
        while idx<len(intervals) and intervals[idx][END] < newInterval[START]:
            new_intervals.append(intervals[idx])
            idx+=1
        start=newInterval[START]
        end=newInterval[END]
        while idx<len(intervals) and (
            (intervals[idx][END] >= start and intervals[idx][END] <= end) or
            (intervals[idx][START] <= end and intervals[idx][END] >= end)
        ):
            start=min(intervals[idx][START],start)
            end=max(intervals[idx][END], end)
            idx+=1
        new_intervals.append([start,end])
        while idx<len(intervals):
            new_intervals.append(intervals[idx])
            idx+=1
        return new_intervals