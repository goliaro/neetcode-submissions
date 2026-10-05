class Solution:
    def maxArea(self, heights: List[int]) -> int:
        compute_area=lambda l,r: min(heights[l],heights[r])*(r-l)
        left,right=0,len(heights)-1
        best_left,best_right=0,len(heights)-1
        while left<right:
            old_area=compute_area(best_left,best_right)
            new_area=compute_area(left,right)
            if new_area>old_area:
                best_left=left
                best_right=right
            else:
                if heights[left]>=heights[right]:
                    right-=1
                else:
                    left+=1
        return compute_area(best_left,best_right)