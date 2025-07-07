class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        edge_set = set()
        queue = deque()
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    edge_set.add((r,c))
                    queue.append((r,c))
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(queue):
            while queue:
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0<=nr<rows and 0<=nc<cols and board[nr][nc] == 'O' and (nr, nc) not in edge_set:
                        edge_set.add((nr,nc))
                        queue.append((nr,nc))

        bfs(queue)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r,c) not in edge_set:
                    board[r][c] = 'X' 