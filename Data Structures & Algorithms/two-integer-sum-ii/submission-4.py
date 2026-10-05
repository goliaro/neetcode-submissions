class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,num in enumerate(numbers):
            match_num = target-num
            # binary search
            left=i+1; right=len(numbers)-1
            match_index=-1
            # print(f"left={left}, right={right}, match_index={match_index}, match_num={match_num}")
            while left<=right:
                mid = (left+right)//2
                # print(f"\tmid={mid}")
                if numbers[mid]==match_num:
                    match_index=mid
                    break
                elif numbers[mid] < match_num:
                    left=mid+1
                else:
                    right=mid-1
            if match_index != -1:
                return [min(i+1,match_index+1), max(i+1,match_index+1)]
        return []