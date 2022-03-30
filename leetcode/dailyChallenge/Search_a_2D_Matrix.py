class Solution:
#     https://leetcode.com/problems/search-a-2d-matrix/
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == target:
                             return True
        return False
