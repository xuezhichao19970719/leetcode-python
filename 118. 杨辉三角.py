class Solution:
    def generate(self, numRows):
        if numRows == 0: return []
        L = [[1]]
        for i in range(numRows-1):
            L.append([sum(m) for m in zip([0]+L[i], L[i]+[0])])
        return L