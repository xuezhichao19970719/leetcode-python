class Solution:
    def levelOrder(self, root):
        ans, level = [], [root]
        while level and root:
            ans.append([node.val for node in level])
            level = [leaf for n in level for leaf in (n.left, n.right) if leaf]
        return ans