class Solution:
    def permuteUnique(self, nums):
        res=list(set(itertools.permutations(nums)))
        res.sort()
        return res