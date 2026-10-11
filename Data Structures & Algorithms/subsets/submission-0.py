class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # initialize subsets to be empty
        # iterate over the number, and add each number to the existing subsets
        result=[[]]
        for num in nums:
            result += [subset+[num] for subset in result]
        return result