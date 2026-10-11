class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub=-math.inf
        cur_sum=0
        for i,n in enumerate(nums):
            max_sub=max(max_sub,n)
            cur_sum += n
            max_sub=max(max_sub,cur_sum)
            if cur_sum < 0:
                cur_sum=max(n,0)
            
        return max_sub