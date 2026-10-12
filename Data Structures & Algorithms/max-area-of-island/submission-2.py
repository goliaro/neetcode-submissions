class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions=[[0,-1], [1,0], [0,1], [-1,0]]
        m,n = len(grid), len(grid[0])
        visited=[[0]*n for _ in range(m)]

        def dfs(x,y) -> int:
            assert visited[x][y] == 0
            assert grid[x][y] == 1
            area=0
            stack=[(x,y)]
            visited[x][y]=1
            while stack:
                x_cur, y_cur = stack.pop()
                area+=1
                for direction in directions:
                    x_new, y_new = x_cur + direction[0], y_cur + direction[1]
                    if x_new >= 0 and x_new < m and y_new >= 0 and y_new < n and visited[x_new][y_new]==0 and grid[x_new][y_new]==1:
                        visited[x_new][y_new]=1
                        stack.append((x_new,y_new))
            return area

        # for each vertex, if it hasn't been visited yet, dfs over it, save max area
        max_area=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    area=dfs(i,j)
                    max_area = max(max_area, area)
        return max_area