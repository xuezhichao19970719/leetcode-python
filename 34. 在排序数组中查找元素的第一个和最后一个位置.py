import bisect


class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        l = bisect.bisect_left(nums, target)
        if l == len(nums) or nums[l] != target:
            l = -1
        r = bisect.bisect_right(nums, target) - 1
        if nums[r] != target:
            r = -1
        return [l, r]