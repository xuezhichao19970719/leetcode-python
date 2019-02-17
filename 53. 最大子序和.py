class Solution:
    def maxSubArray(self, nums):
        s = 0
        m = nums[0]
        for num in nums:
            s += num
            if s > m:
                m = s
            if s < 0:
                s = 0
        return m
        