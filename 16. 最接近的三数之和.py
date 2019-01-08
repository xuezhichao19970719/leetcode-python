class Solution:
    def threeSumClosest(self, nums, target):
        res = []
        a = abs(nums[0] + nums[1] + nums[2] - target) + 1
        nums.sort()
        x = len(nums) - 1
        for i in range(x):
            if i == 0 or nums[i] > nums[i-1]:
                l = i + 1
                r = x
                while l < r:
                    s = nums[i] + nums[l] + nums[r] - target
                    if s < 0:
                        l += 1 
                    elif s > 0:
                        r -= 1
                    else:
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    if abs(s) < a:
                        a = abs(s)
                        res.append(s + target)
        return res[-1]