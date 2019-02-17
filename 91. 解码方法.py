class Solution:
    def numDecodings(self, s):
        v = 0
        w = int(s>'')
        p = ''
        for d in s:
            v, w = w, (d>'0')*w + (9<int(p+d)<27)*v
            p = d
        return w