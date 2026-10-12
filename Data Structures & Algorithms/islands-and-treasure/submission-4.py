class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # run multi-source bfs from each grid item marked as 0
        m,n = len(grid), len(grid[0])
        directions=[[0,-1],[0,1], [-1,0], [1,0]]

        visited=[[0]*n for _ in range(m)]
        queue=deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visited[i][j]=1
        # print(f"m={m},n={n}")
        # print(f"initialized queue with {len(queue)} elements")
        while len(queue) > 0:
            x,y=queue.popleft()
            # print(f"cur el: ({x},{y})")
            for direction in directions:
                x_new, y_new = x + direction[0], y+direction[1]
                # print(f"\tneighbor: ({x_new},{y_new})")
                # if (x_new >=0 and x_new<m and y_new>=0 and y_new<n):
                #     print(f"\tvisited={visited[x_new][y_new]} grid={grid[x_new][y_new]}")
                if x_new < 0 or x_new >= m or y_new < 0 or y_new >= n or visited[x_new][y_new]==1 or grid[x_new][y_new] == -1 or grid[x_new][y_new]==0:
                    continue
                # print(f"\tupdating ({x_new},{y_new})")
                grid[x_new][y_new]=min(grid[x_new][y_new], grid[x][y]+1)
                queue.append((x_new,y_new))
                visited[x_new][y_new]=1