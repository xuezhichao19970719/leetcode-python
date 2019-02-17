class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder: return
        root = TreeNode(preorder.pop(0))
        index = inorder.index(root.val)
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index + 1:])
        return root