# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(root, upper, lower):
            if root is None:
                return True

            if lower != None and root.val <= lower:
                return False
            if upper != None and root.val >= upper:
                return False

            if not dfs(root.left, root.val, lower):
                return False
            if not dfs(root.right, upper, root.val):
                return False
            return True
        return dfs(root, None, None)





