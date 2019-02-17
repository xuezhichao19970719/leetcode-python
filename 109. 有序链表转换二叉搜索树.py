class Solution:
    def sortedArrayToBST(self, nums):
        if not nums: return
        mid=len(nums)>>1
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
    def sortedListToBST(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.sortedArrayToBST(nums)
        