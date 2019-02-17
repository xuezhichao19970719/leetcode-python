class Solution:
    def subsetsWithDup(self, nums):
        l = []
        for i in range(len(nums) + 1):
            l += map(lambda x:tuple(sorted(x)), itertools.combinations(nums, i))
        return list(map(list,set(l)))
        
        