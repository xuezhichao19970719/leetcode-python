class Solution:
    def divide(self, dividend, divisor):
        s = (dividend>0) == (divisor>0)
        dividend,divisor = abs(dividend),abs(divisor)
        res=0
        while dividend>=divisor:
            tmp,i = divisor,1
            while dividend >= tmp:
                dividend -= tmp
                res+=i
                tmp = tmp<<4
                i = i<<4
        if not s:
            res = -res
        return min(max(-2147483648,res), 2147483647)