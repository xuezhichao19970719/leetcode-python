class Solution:
    def setZeroes(self, matrix):
        m = range(len(matrix))
        n = len(matrix[0])
        o = set()
        p = set()
        for i in m:
            for j in range(n):
                if matrix[i][j] == 0:
                    o.add(i)
                    p.add(j)
        for i in o:
            matrix[i] = [0]*n
        for j in p:
            for i in set(m) - o:
                matrix[i][j] = 0
        return
            