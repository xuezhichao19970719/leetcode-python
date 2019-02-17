class Solution:
    def subsets(self, nums):
        l = []
        for i in range(len(nums)+1):
            l += itertools.combinations(nums, i)
        return l