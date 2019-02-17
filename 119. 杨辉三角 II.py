class Solution:
    def getRow(self, rowIndex):
        L = [1]
        for i in range(rowIndex):
            L = [sum(m) for m in zip([0]+L, L+[0])]
        return L