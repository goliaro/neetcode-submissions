class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # level-by-level multi-source traversal
        m,n = len(grid), len(grid[0])
        directions=[[0,-1], [0,1], [-1,0], [1,0]]

        queue=deque([])
        # visited=[[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    # visited[i][j]=1
        level=0
        while len(queue) > 0:
            new_level=deque([])
            for x,y in queue:
                assert grid[x][y] == 2
                for direction in directions:
                    x_new, y_new = x + direction[0], y + direction[1]
                    if x_new < 0 or x_new >=m or y_new < 0 or y_new >=n or grid[x_new][y_new] != 1:
                        continue
                    grid[x_new][y_new]=2
                    new_level.append((x_new,y_new))
            if len(new_level) >0:
                level+=1
            queue=new_level
        # print(grid)
        # print(level)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return level
