class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_run=0
        last_num=-1
        current_run=0
        for i,num in enumerate(sorted(nums)):
            if i==0:
                last_num=num
                current_run=1
                longest_run=1
            else:
                if num == last_num:
                    continue
                elif num == last_num+1:
                    current_run +=1
                    last_num=num
                    longest_run = max(current_run, longest_run)
                else:
                    longest_run = max(current_run, longest_run)
                    last_num=num
                    current_run=1
        return longest_run