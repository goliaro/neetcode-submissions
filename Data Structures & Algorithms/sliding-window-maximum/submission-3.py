import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # populate max heap with initial window, save max
        # at each step, add new item, set left item to deleted
        # get max (if deleted, pop until done)
        # heap = []
        # deleted = {}
        # for i in range(k):
        #     heapq.heappush(heap, -nums[i])
        # l=0; r=k
        # maxes = [0]*(len(nums)-k+1)
        # maxes[0] = -heap[0]
        # while r<len(nums):
        #     heapq.heappush(heap, -nums[r])
        #     deleted[-nums[l]] = deleted.get(-nums[l],0) +1
        #     r+=1; l+=1
        #     # peak the top. clear the deleted ones only
        #     top=heap[0]
        #     while top in deleted:
        #         deleted[top] -= 1
        #         if deleted[top] == 0:
        #             del deleted[top]
        #         heapq.heappop(heap)
        #         top=heap[0]
        #     maxes[l] = -top
        # return maxes



        heap = [(-nums[i],i) for i in range(k)]
        heapq.heapify(heap)

        maxes = [-heap[0][0]]
        r=k #(exclusive)
        while r < len(nums):
            heapq.heappush(heap, (-nums[r], r))

            # remove all items that have fallen out of window
            while heap[0][1] <= r-k:
                heapq.heappop(heap)
            
            maxes.append(-heap[0][0])

            r+=1
        return maxes