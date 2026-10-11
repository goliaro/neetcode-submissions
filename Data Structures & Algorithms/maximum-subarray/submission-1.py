class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        cur_sum=0
        for n in nums:
            # if sum has gotten negative, we should drop it and start a new interval
            cur_sum=max(cur_sum, 0)
            # add current item to interval (new or old one)
            cur_sum += n
            # check if this is best
            max_sub=max(max_sub,cur_sum)
        return max_sub