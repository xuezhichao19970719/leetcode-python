class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        res, n, limit = [], len(nums), target/4
        for i in range(n-3):
            if nums[i] > limit:
                break
            if i != 0 and nums[i] == nums[i-1]:
                continue
            for j in range(n-1,i+2,-1):
                if nums[j] < limit:
                    break
                if j != n -1 and nums[j] == nums[j+1]:
                    continue
                lo, hi, sum2 = i + 1, j - 1, nums[i] + nums[j] 
                limit2 = (target - sum2)/2
                while lo < hi and nums[lo] <= limit2 and nums[hi] >= limit2:
                    sum = sum2 + nums[lo] + nums[hi] 
                    if sum == target:
                        res += (nums[i], nums[lo], nums[hi], nums[j]),
                        while lo < hi and nums[hi] == nums[hi-1]:
                            hi -= 1
                        while lo < hi and nums[lo] == nums[lo+1]:
                            lo += 1
                    lo += sum <= target
                    hi -= sum >= target
        return res