class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific_set = set()
        atlantic_set = set()
        pacific_queue = deque()
        atlantic_queue = deque()

        for i in range(cols):
            pacific_set.add((0,i))
            pacific_queue.append((0,i))
            atlantic_set.add((rows-1, i))
            atlantic_queue.append((rows-1, i))

        for i in range(rows):
            pacific_set.add((i,0))
            pacific_queue.append((i,0))
            atlantic_set.add((i, cols-1))
            atlantic_queue.append((i, cols-1))

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(queue, visited):
            while queue:
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols and heights[nr][nc] >= heights[r][c] and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
        
        bfs(pacific_queue, pacific_set)
        bfs(atlantic_queue, atlantic_set)

        return list(pacific_set & atlantic_set)
