class Solution:
    def getPermutation(self, n, k):
        FAC = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        res = 0
        k -= 1
        nums = list(range(1, n + 1))
        for i in range(n):
            cs, k = divmod(k, FAC[n - i - 1])
            res = 10 * res + nums[cs]
            del nums[cs]
        return str(res)