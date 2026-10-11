class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) ==1:
            return stones[0]
        q=[-s for s in stones]
        heapq.heapify(q)
        while len(q) > 1:
            first = heapq.heappop(q)
            second = heapq.heappop(q)
            if first != second:
                heapq.heappush(q,-abs(first-second))
        if len(q) == 1:
            return -heapq.heappop(q)
        else:
            return 0