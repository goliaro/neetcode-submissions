class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i,num in enumerate(numbers):
        #     match_num = target-num
        #     # binary search
        #     left=i+1; right=len(numbers)-1
        #     match_index=-1
        #     while left<=right:
        #         mid = (left+right)//2
        #         if numbers[mid]==match_num:
        #             match_index=mid
        #             break
        #         elif numbers[mid] < match_num:
        #             left=mid+1
        #         else:
        #             right=mid-1
        #     if match_index != -1:
        #         return [min(i+1,match_index+1), max(i+1,match_index+1)]
        # return []
        left, right = 0, len(numbers)-1
        while left<right:
            s = numbers[left] + numbers[right]
            if s==target:
                return [left+1,right+1]
            if s > target:
                right-=1
            else:
                left+=1
        return []
