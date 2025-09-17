class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        n = len(grid)
        m = len(grid[0])
        visited = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(i,j):
            queue = deque()
            queue.append((i,j))
            visited.add((i,j))
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '1' and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i,j) not in visited:
                    bfs(i,j)
                    islands += 1
        
        return islands