# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.max_path = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root):
            if root is None:
                return 0

            leftGain = max(dfs(root.left), 0)
            rightGain = max(dfs(root.right), 0)

            gain = root.val + leftGain + rightGain
            if gain > self.max_path:
                self.max_path = gain

            return root.val + max(leftGain, rightGain)
        dfs(root)
        return self.max_path

