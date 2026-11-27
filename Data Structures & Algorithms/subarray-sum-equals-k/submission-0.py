class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        num_prefixes={0:1} # key: sum, value: count
        prefix_sum = 0
        res=0
        
        # prefix_sum[i] - prefix_sum[j] == k -> subarray[j:i] sums to k
        # when we are at position i, we just need to know all indices j whose prefix sums equal prefix_sum[i]-k, then we can add that amount to res
        
        for i,n in enumerate(nums):
            prefix_sum += n
            
            if prefix_sum-k in num_prefixes:
                res += num_prefixes[prefix_sum-k]
            
            num_prefixes[prefix_sum] = num_prefixes.get(prefix_sum, 0) + 1
        return res