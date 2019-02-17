class Solution:
    def firstMissingPositive(self, nums):
        length = len(nums)
        k = 0
        for i, num in enumerate(nums):
            if num > 0 and num <= length:
                nums[k] = num 
                k += 1 
        for i in range(k):
            num = abs(nums[i])
            
            if nums[num-1] > 0:
                nums[num-1] *= -1
        for i in range(k):
            if nums[i] >= 0:
                return i+1
        return k+1