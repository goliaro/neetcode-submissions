def ceildiv(a,b):
    return int((a+b-1)/b)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=ceildiv(sum(piles), h)
        high=max(piles)
        # print(f"low={low}, high={high}")
        while low<high:
            mid=(low+high)//2

            tot_time=sum([ceildiv(p,mid) for p in piles])
            if tot_time<=h:
                high= mid
            else:
                low=mid+1
            # else:
            #     low=mid+1
        return low
