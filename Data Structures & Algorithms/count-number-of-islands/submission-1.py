class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        visited=[[0]*n for _ in range(m)]

        directions=[[0,-1], [1,0], [0,1], [-1,0]]

        connected_components=0

        def dfs(i,j):
            stack=[(i,j)]
            while stack:
                a,b=stack.pop()
                visited[a][b] = 1
                for direction in directions:
                    x_new, y_new = a+direction[0], b+direction[1]
                    if x_new >= 0 and x_new < m and y_new >= 0 and y_new <n:
                        if grid[x_new][y_new] == "1" and visited[x_new][y_new] == 0:
                            stack.append((x_new, y_new))

        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                if visited[i][j] == 0:
                    connected_components+=1
                    dfs(i,j)
        return connected_components