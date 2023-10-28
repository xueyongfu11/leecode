# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        k_list = []

        def dfs(root, k):
            if root is None:
                k_list.append(k)
                return

            dfs(root.left, k + 1)
            dfs(root.right, k + 1)

        dfs(root, 0)

        max_d = max(k_list)
        return max_d