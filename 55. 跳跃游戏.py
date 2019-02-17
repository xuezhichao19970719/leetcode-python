class Solution:
    def canJump(self, nums):
        m = 0
        b = len(nums)
        for i in range(b):
            if i > m:
                return False
            if i+nums[i]>m:
                m = i+nums[i]
            if m >= b-1:
                return True