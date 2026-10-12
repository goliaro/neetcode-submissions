class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid), len(grid[0])
        directions=[[0,-1], [0,1], [-1,0],[1,0]]
        
        def bfs(x,y):
            assert grid[x][y] == 0
            queue=deque()
            queue.append((x,y))
            # visited=[[0]*n for _ in range(m)]
            # visited[x][y]=1
            while queue:
                x_cur, y_cur = queue.popleft()
                for direction in directions:
                    x_new, y_new = x_cur + direction[0], y_cur + direction[1]
                    if x_new < 0 or x_new >= m or y_new < 0 or y_new >= n:
                        continue
                    # if visited[x_new][y_new] == 1:
                    #     continue
                    if grid[x_new][y_new] > grid[x_cur][y_cur] +1:
                        grid[x_new][y_new] = grid[x_cur][y_cur] +1
                        queue.append((x_new, y_new))
                        # visited[x_new][y_new] = 1
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0:
                    bfs(x,y)
        
