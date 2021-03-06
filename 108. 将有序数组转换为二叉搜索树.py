class Solution:
    def sortedArrayToBST(self, nums):
        if not nums: return
        mid=len(nums)>>1
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
        