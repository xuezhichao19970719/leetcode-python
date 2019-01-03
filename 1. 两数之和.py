class Solution:
    def twoSum(self, nums, target):
        a ={}
        for i, num in enumerate(nums):
            if target-num in a:
                return [a[target - num], i]
            else:
                a[num] = i