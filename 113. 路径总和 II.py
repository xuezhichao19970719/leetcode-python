class Solution:
    def pathSum(self, root, sum):
        if not root: return []
        if root.left == root.right == None:
            return [[root.val]] if sum == root.val else []
        a = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)
        return [[root.val] + i for i in a]