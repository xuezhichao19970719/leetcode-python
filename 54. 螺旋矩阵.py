class Solution:
    def spiralOrder(self, matrix):
        a = []
        while matrix:
            a += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return a
        