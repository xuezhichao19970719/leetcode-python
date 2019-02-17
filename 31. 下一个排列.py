class Solution:
    def nextPermutation(self, nums):
        l=len(nums)
        for i in range(l-2,-1,-1):
            for j in range(l-1,i,-1):
                if nums[j]>nums[i]:
                    nums[j],nums[i]=nums[i],nums[j]
                    nums[i+1:l]=sorted(nums[i+1:l])
                    return
        nums.sort()
        return 