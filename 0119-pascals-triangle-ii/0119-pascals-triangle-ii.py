class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        for i in range(rowIndex+1):
            rows = [1] * (i+1)
            for j in range(1,i):
                rows[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(rows)
        return triangle[-1]