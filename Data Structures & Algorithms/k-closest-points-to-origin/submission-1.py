class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances=[]
        heapq.heapify(distances)

        for point in points:
            x,y=point
            d = x**2 + y**2
            heapq.heappush(distances,(d,point))
        # print(distances)
        result=[]
        for _ in range(k):
            t = heapq.heappop(distances)
            result.append(t[1])
        return result
        # return [x[1] for x in ]