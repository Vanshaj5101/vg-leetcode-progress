class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = (m*n)-1
        while l<=r:
            mid = (r+l)//2
            x = mid // n
            y = mid % n
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                l += 1
            else:
                r -= 1
        return False