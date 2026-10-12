class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        visited=[[0]*n for _ in range(m)]

        connected_components=0

        def dfs(i,j):
            stack=[(i,j)]
            while stack:
                a,b=stack.pop()
                visited[a][b] = 1
                if b-1>=0:
                    if grid[a][b-1] == "1" and visited[a][b-1] == 0:
                        stack.append((a,b-1))
                if a+1<m:
                    if grid[a+1][b] == "1" and visited[a+1][b] == 0:
                        stack.append((a+1,b))
                if b+1<n:
                    if grid[a][b+1] == "1" and visited[a][b+1] == 0:
                        stack.append((a,b+1))
                if a-1>=0:
                    if grid[a-1][b] == "1" and visited[a-1][b] == 0:
                        stack.append((a-1,b))

        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                if visited[i][j] == 0:
                    connected_components+=1
                    dfs(i,j)
        return connected_components