class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        res=[]
        for i,num in enumerate(nums):
            if num > 0:
                # we cannot get a sum of 0, since everything to the right will be > 0
                break
            if i>0 and num == nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                s=nums[left]+nums[right]+num
                if s==0:
                    res.append([num,nums[left],nums[right]])
                    l=nums[left]
                    r=nums[right]
                    while left<right and nums[left]==l:
                        left+=1
                    while left<right and nums[right]==r:
                        right-=1
                elif s>0:
                    right-=1
                else:
                    left+=1
        return res
                