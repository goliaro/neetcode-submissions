class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_costs=[math.inf]*(len(cost)+1)
        min_costs[0]=0
        min_costs[1]=0
        for i,c in enumerate(cost):
            if i+1<(len(cost)+1):
                min_costs[i+1] = min(min_costs[i+1], min_costs[i]+c)
            if i+2<(len(cost)+1):
                min_costs[i+2] = min(min_costs[i+2], min_costs[i]+c)
        return min_costs[-1]