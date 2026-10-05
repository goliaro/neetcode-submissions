class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods_left=[1]*len(nums)
        prods_right=[1]*len(nums)
        for i,n in enumerate(nums):
            if i<len(nums)-1:
                prods_left[i+1] = prods_left[i]*n
        for i in range(len(nums)-1, -1, -1):
            if i>0:
                prods_right[i-1] = prods_right[i] * nums[i]
        assert(len(prods_left) == len(prods_right))
        # print(prods_left)
        # print(prods_right)
        return [prods_left[i]*prods_right[i] for i in range(len(prods_left))]