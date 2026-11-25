class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        cum_max_left = [0]*l
        cum_max_right = [0]*l
        for i,h in enumerate(height):
            if i<l-1:
                cum_max_left[i+1] = max(cum_max_left[i], height[i])
        for i,h in enumerate(reversed(height)):
            if i < l-1:
                cum_max_right[l-i-2] = max(cum_max_right[l-i-1], height[l-i-1])
        
        rain = [
            max(min(cum_max_left[i], cum_max_right[i])-h, 0)
            for i,h in enumerate(height)
        ]
        # print(cum_max_left)
        # print(cum_max_right)
        # print(rain)
        return sum(rain)
