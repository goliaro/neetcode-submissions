"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # this is asking us for the maximum number of overlapping meetings
        # create a dictionary with keys=start/end times of each meeting
        # those are events. if starting, value +=1, if ending value -=1
        # go over all the keys (times) in order, and keep track of current number of open meetings
        events={}
        for interval in intervals:
            events[interval.start] = events.get(interval.start,0)+1
            events[interval.end] = events.get(interval.end,0)-1
        current_meetings=0
        max_meetings=0
        for event, delta in sorted(events.items(), key=lambda x: x[0]):
            current_meetings += delta
            assert current_meetings >= 0 and current_meetings <= len(intervals)
            max_meetings = max(max_meetings, current_meetings)
        assert current_meetings == 0
        return max_meetings