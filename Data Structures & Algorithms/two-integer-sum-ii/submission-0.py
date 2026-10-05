class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,num in enumerate(numbers):
            match_num = target-num
            # binary search
            left=0; right=len(numbers)-1
            match_index=-1
            while left<right:
                mid = (left+right)//2
                if numbers[mid]==match_num and mid !=i:
                    match_index=mid
                    break
                elif numbers[mid] < match_num:
                    left=mid+1
                else:
                    right=mid
            if match_index != -1:
                return [min(i+1,match_index+1), max(i+1,match_index+1)]
