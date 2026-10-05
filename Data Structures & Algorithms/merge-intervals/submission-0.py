class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals)
        new_intervals=[]
        i=0
        START=0;END=1
        while i<len(intervals):
            if i==len(intervals)-1:
                new_intervals.append(intervals[i])
                break
            if intervals[i][END]<intervals[i+1][START]:
                new_intervals.append(intervals[i])
                i+=1
            else:
                # iterate until reaching the first interval that starts after current end
                start=intervals[i][START]
                end=intervals[i][END]
                i+=1
                while i<len(intervals):
                    if intervals[i][START] > end:
                        break
                    else:
                        end=max(end, intervals[i][END])
                        i+=1
                new_intervals+=[[start,end]]
        return new_intervals 