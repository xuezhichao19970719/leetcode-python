class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder: return
        root = TreeNode(postorder.pop())
        index = inorder.index(root.val)
        root.right = self.buildTree(inorder[index + 1:], postorder)
        root.left = self.buildTree(inorder[:index], postorder)
        return root