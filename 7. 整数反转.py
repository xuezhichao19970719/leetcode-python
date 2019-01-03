class Solution:
    def reverse(self, x):
        a = int(''.join(list(str(abs(x))[::-1])))
        if a < -2**31 or a > 2**31 - 1:
            return 0
        if x >-1:
           return a
        if x < 0:
            return -a