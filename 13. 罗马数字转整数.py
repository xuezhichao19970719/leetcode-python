class Solution:
    def romanToInt(self, s):
        d={'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        res = 0
        p = 'I'
        for c in s[::-1]:
            res = res - d[c] if d[c] < d[p] else res + d[c]
            p = c
        return res