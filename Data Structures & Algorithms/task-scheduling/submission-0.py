from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # sort by frequency (descending)
        # keep them in a max heap by current frequency
        # if freq>1, put into cool down dict, where you store last position inserted
        tasks_with_freqs=Counter(tasks)
        tasks_heap=[]
        heapq.heapify(tasks_heap)
        for task in tasks_with_freqs:
            frequency=tasks_with_freqs[task]
            heapq.heappush(tasks_heap, (-frequency,task))
        
        cool_down={} # index -> list of (task, frequency) being released
        index=0
        while len(tasks_heap) > 0 or len(cool_down) > 0:
            # if anything finished cooling down, put back into the heap
            if index in cool_down:
                for task_pair in cool_down[index]:
                    heapq.heappush(tasks_heap, task_pair)
                del cool_down[index]
            
            # if there is anything in the heap, schedule it
            if len(tasks_heap) > 0:
                neg_freq,task = heapq.heappop(tasks_heap)
                assert neg_freq <= -1
                if neg_freq < -1:
                    if index+n+1 in cool_down:
                        cool_down[index+n+1].append((neg_freq+1,task))
                    else:
                        cool_down[index+n+1]=[(neg_freq+1,task)]
            index+=1
        return index
