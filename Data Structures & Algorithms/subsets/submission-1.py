class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # initialize subsets to be empty
        # iterate over the number, and add each number to the existing subsets
        # result=[[]]
        # for num in nums:
        #     result += [subset+[num] for subset in result]
        # return result


        # binary way
        n = len(nums)
        res=[]
        for i in range(2**n):
            # is a number, we insert item j in the subset if bit j is set to 1
            subset=[]
            for j in range(n):
                if i & (1<<j):
                    subset.append(nums[j])
            res.append(subset)
        return res