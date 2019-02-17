class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0] or target < matrix[0][0] or target > matrix[-1][-1]: return False
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                break
        return target in matrix[i]