class TimeMap:

    def __init__(self):
        self.kv_store={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.kv_store:
            self.kv_store[key].append((timestamp,value))
        else:
            self.kv_store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv_store:
            return ""
        entry = self.kv_store[key]
        assert len(entry) > 0
        if timestamp > entry[-1][0]:
            return entry[-1][1]
        elif timestamp < entry[0][0]:
            return ""
        else:
            # binary search
            low, high = 0, len(entry)
            while low < high:
                mid = (low+high)//2
                if entry[mid][0] == timestamp:
                    return entry[mid][1]
                elif entry[mid][0] > timestamp:
                    high = mid
                else:
                    low=mid+1
            return entry[low-1][1]
        
