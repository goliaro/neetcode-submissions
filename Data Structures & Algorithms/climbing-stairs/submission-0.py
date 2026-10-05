class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        ways=[1]*(n+1)
        for i in range(2,n+1):
            ways[i]=ways[i-1]+ways[i-2]
        return ways[n]