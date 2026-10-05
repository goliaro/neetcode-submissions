class Solution:
    
    # TIME: O(n + n*log n)= O(n log n)
    # SPACE: O(n)
    def naive(self, nums,k):
        freqs={}
        for num in nums:
            freqs[num]=freqs.get(num,0)+1
        return [f[0] for f in sorted(freqs.items(),key=lambda x:-x[1])[:k]]
    
    def heap(self,nums,k):
        freqs={}
        for num in nums:
            freqs[num]=freqs.get(num,0)+1
        heap=[]
        for n,f in freqs.items():
            heapq.heappush(heap,(f,n))
            if len(heap) > k:
                heapq.heappop(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
        
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return naive(self,nums,k)
        return self.heap(nums,k)