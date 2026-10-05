class Solution:
    def maxArea(self, heights: List[int]) -> int:
        compute_area=lambda l,r: min(heights[l],heights[r])*(r-l)
        left,right=0,len(heights)-1
        best_area=0
        while left<right:
            new_area=compute_area(left,right)
            best_area=max(new_area,best_area)
            if heights[left]>=heights[right]:
                right-=1
            else:
                left+=1
        return best_area