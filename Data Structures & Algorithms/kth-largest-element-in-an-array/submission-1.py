class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # using sorting
        # return sorted(nums)[-k]
        # using heap
        biggest=[]
        heapq.heapify(biggest)
        for num in nums:
            heapq.heappush(biggest, -num)
        for _ in range(k-1):
            heapq.heappop(biggest)
        return -heapq.heappop(biggest)
